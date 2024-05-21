from mtcnn import MTCNN


def detectFace(photo):
    classifier = MTCNN()

    res = classifier.detect_faces(photo)

    if res:
        return True
    else:
        return False
