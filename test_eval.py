from pycocoevalcap.eval import COCOEvalCap
from pycocotools.coco import COCO


def _coco_evaluation(predicts, answers):
    coco_res = []
    ann = {'images': [], 'info': '', 'type': 'captions', 'annotations': [], 'licenses': ''}

    for i, (predict, answer) in enumerate(zip(predicts, answers)):
        #predict_cap = ' '.join(predict)
        #answer_cap = ' '.join(answer).replace('_UNK', '_UNKNOWN')

        ann['images'].append({'id': i})
        ann['annotations'].append({'caption': answer, 'id': i, 'image_id': i})
        coco_res.append({'caption': predict, 'id': i, 'image_id': i})

    coco = COCO(ann)
    coco_res = coco.loadRes(coco_res)
    coco_eval = COCOEvalCap(coco, coco_res)
    coco_eval.evaluate()

    return coco_eval.eval


def main():
    predicts = ['i am a boy',
                'she is a girl']
    answers = ['am i a boy ?',
               'is she a girl ?']
    eval_results = _coco_evaluation(predicts, answers)
    print(eval_results)


if __name__ == '__main__':
    main()
