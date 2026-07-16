import av
import cv2


class VideoProcessor:

    def recv(self, frame):

        image = frame.to_ndarray(format="bgr24")

        cv2.putText(
            image,
            "HELLO FROM VIDEO PROCESSOR",
            (40, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )

        return av.VideoFrame.from_ndarray(
            image,
            format="bgr24"
        )