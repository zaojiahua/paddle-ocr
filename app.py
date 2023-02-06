from datetime import datetime

import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr

app = Flask(__name__)
CORS(app, expose_headers=["*"])

ocr_ch = PaddleOCR(use_angle_cls=True, lang="ch")


@app.route("/test", methods=["GET"])
def test_ocr():
    return render_template('test.html', url=f"{url_for('ocr')}")


@app.route("/ocr", methods=["POST"])
def ocr():
    file = request.files.get("image_body")
    words = request.form.to_dict().get("words")
    is_second = request.form.to_dict().get("is_second", False)
    try:
        words = request.json.get("words") if hasattr(request, 'json') else words
        is_second = request.json.get("is_second", False) if hasattr(request, 'json') else is_second
        if file is None:
            file = request.json.get("image_path")
    except Exception as e:
        print(e)
    print(file, words, is_second)

    if file is None:
        return jsonify({"status": "fail", "reason": "no image", "status_code": 3001}), 400

    return ocr_identify(file, words, is_second)


def ocr_identify(image_path, words=None, is_second=False):
    try:
        image = Image.open(image_path)
        image_array = np.array(image)
        # result, box_list = text_predict(image_array, searching_words=words, is_second=is_second)
        result = ocr_ch.ocr(image_array, cls=True)
        box_list = []
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                left_top = line[0][0]
                right_bottom = line[0][2]
                text = line[1][0]
                box = {'text': text,
                       'cx': (left_top[0] + right_bottom[0]) / 2,
                       'cy': (left_top[1] + right_bottom[1]) / 2}
                if words is not None and text == words:
                    box_list = box
                    break
                elif words is None:
                    box_list.append(box)
            if words is not None and box_list:
                break

        if words is not None and not box_list:
            return {"status": "not found"}, []

        return jsonify(result=box_list, status='success'), 200
    except Exception as e:
        try:
            cv2.imwrite(f"{datetime.now().strftime('%m-%d-%H_%M_%S')}error.jpg", image_array)
        except Exception:
            image.save(f"{datetime.now().strftime('%m-%d-%H_%M_%S')}error-raw.png")
        finally:
            return jsonify({"status": "fail", "reason": repr(e), "status_code": 3000}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
