# Librerias
import math
import cv2
import mediapipe as mp
import time

# Clases


class detector_manos:
    def __init__(
        self,
        mode=False,
        maxManos=2,
        model_complexity=1,
        Confdeteccion=0.5,
        Confsegui=0.5,
    ):
        self.mode = mode
        self.maxManos = maxManos
        self.compl = model_complexity
        self.Confdeteccion = Confdeteccion
        self.Confsegui = Confsegui

        # objetos que detecta las manos y la dibujan

        self.mpmanos = mp.solutions.hands
        self.manos = self.mpmanos.Hands(
            self.mode, self.maxManos, self.compl, self.Confdeteccion, self.Confsegui
        )
        self.dibujo = mp.solutions.drawing_utils
        self.tip = [4, 8, 12, 16, 20]

    # Funcion para detectar la mano

    def encontrar_manos(self, frame, dibujar=True):
        imgcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.resultados = self.manos.process(imgcolor)

        if self.resultados.multi_hand_landmarks:
            for mano in self.resultados.multi_hand_landmarks:
                if dibujar:
                    self.dibujo.draw_landmarks(
                        frame, mano, self.mpmanos.HAND_CONNECTIONS
                    )
        return frame

    #  Funcion para dectectar la posicion de la mano

    def encontrar_posicion(self, frame, ManoNum=0, dibujar=True, color=[]):
        xlista = []
        ylista = []
        bbox = []
        player = 0

        self.lista = []
        if self.resultados.multi_hand_landmarks:
            miMano = self.resultados.multi_hand_landmarks[ManoNum]
            prueba = self.resultados.multi_hand_landmarks
            player = len(prueba)

            # imprime el jugador

            for id, lm in enumerate(miMano.landmark):
                alto, ancho, c = frame.shape  # Extrae dimensiones
                cx, cy = int(lm.x * ancho), int(lm.y * alto)
                xlista.append(cx)
                ylista.append(cy)
                self.lista.append([id, cx, cy])
                if dibujar:
                    cv2.circle(frame, (cx, cy), 3, (0, 0, 0), cv2.FILLED)

            xmin, xmax = min(xlista), max(xlista)
            ymin, ymax = min(ylista), max(ylista)
            bbox = xmin, ymin, xmax, ymax
            if dibujar:
                cv2.rectangle(
                    frame, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), color, 2
                )
        return self.lista, bbox, player

    # Deteccion dedos arriba

    def dedos_arriba(self):
        dedos = []
        if self.lista[self.tip[0]][1] > self.lista[self.tip[0] - 1][1]:
            dedos.append(1)
        else:
            dedos.append(0)

        for id in range(1, 5):
            if self.lista[self.tip[id]][2] < self.lista[self.tip[id] - 2][2]:
                dedos.append(1)
            else:
                dedos.append(0)

        return dedos

    # deteccion distancia entre dedos

    def distancia(self, p1, p2, frame, dibujar=True, r=15, t=3):
        x1, y1 = self.lista[p1][1:]
        x2, y2 = self.lista[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        if dibujar:
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), t)
            cv2.circle(frame, (x1, y1), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, frame, [x1, y1, x2, y2, cx, cy]


def main():
    ptiempo = 0
    ctiempo = 0

    cap = cv2.VideoCapture(0)

    detector = detector_manos()

    while True:
        ret, frame = cap.read()

        frame = detector.encontrar_posicion(frame)
        lista, bbox = detector.encontrar_posicion(frame)
        # if len(lista) ! = 0:
        #    print(lista[4])

        ctiempo = time.time()
        fps = 1 / (ctiempo - ptiempo)
        ptiempo = ctiempo

        cv2.putText(
            frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
        )

        cv2.imshow("Manos", frame)
        k = cv2.waitKey(1)

        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
