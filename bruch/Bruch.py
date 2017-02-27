import mock

class Bruch(object):
    """
    Diese Klasse berechnet sich Brüche mit unterschiedlichsten Operatoren wie Division oder Addition.
    """
    def __init__(self,zaehler,nenner=1):
        """
        Der Konstruktor von Bruch. Floats werden hier noch nicht erlaubt da dies (und andere types)
        in den folgenden Operatoren behandelt wird.
        :param zaehler: Der Zaehler des Bruches
        :param nenner: Der Nenner des Buches
        """
        self.zaehler = zaehler
        self.nenner = nenner
        if self.nenner == 0:
            raise ZeroDivisionError
        if type(self.nenner) == float or type(self.zaehler) == float:
            raise TypeError

    def __float__(self):
        """
        Dividiert Zaehler und Nenner und gibt das Ergebnis als float aus.
        :return: Gibt eine Gleitkommazahl zurück
        """
        ergebnis=float(self.zaehler) / float(self.nenner)
        return float(ergebnis)

    def __int__(self):
        """
        Dividiert Zaehler und Nenner und gibt das Ergebnis als int aus.
        :return: Gibt ein Ganzzahliges Ergebnis zurück
        """
        ergebnis = self.zaehler / self.nenner
        return int (ergebnis)

    def __complex__(self):
        """
        Dividiert Zaehler und Nenner und gibt das Ergebnis als complex aus.
        :return: Gibt eine Gleitkommazahl aus
        """
        ergebnis = self.zaehler / self.nenner
        return complex(ergebnis)

    def __invert__(self):
        """
        Nimmt Zaehler und Nenner und vertauscht sie.
        :return: Gibt den Bruch invertiert zurück
        """
        return Bruch(self.nenner, self.zaehler)

    def __abs__(self):
        """
        Nimmt einen Bruch entgegen (egal ob positiv oder negativ) und gibt ihn als positiven Bruch zurück.
        :return: Gibt einen positiven Bruch zurück
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        Nimmt einen Bruch entgegen und gibt ihn als negativen Bruch zurück
        :return: Gibt einen negativen Bruch zurück
        """
        return Bruch(-self.zaehler,self.nenner)

    def __pow__(self, power, modulo=None):
        """
        Nimmt einen Bruch und eine Hochzahl entgegen und berechnet sich diesen Bruch.
        :param power: Wie oft die Zahl mit sich selbst multipliziert werden soll
        :param modulo: Keine
        :return: Gibt den Bruch^power zurück
        """
        if type(power) == float:
            raise TypeError
        return Bruch(self.zaehler ** power, self.nenner ** power)

    @classmethod
    def __makeBruch(cls, value):
        """
        Nimmt einen Wert entgegen und wandelt diesen Wert in einen Bruch um.
        :param value: Der Wert der in einen Bruch umgewandelt werden soll
        :return: Gibt einen Bruch mit dem value als Zaehler zurück
        """
        if type(value) == int:
            return Bruch(value)
        else:
            raise TypeError

    def __eq__(self, other):
        """
        Überprüft ob beide Brüche gleich sind
        :param other: Der Bruch mit dem verglichen werden soll
        :return: Gibt True zurück wenn beide Brüche gleich sind und False falls sie nicht übereinstimmen
        """
        return float(self) == float(other)

    def __str__(self):
        """
        Wandelt einen int/float Bruch in einen String um.
        :return: Gibt einen String mit dem Bruch zurück "(Zeahler/Nenner)"
        """
        if (self.zaehler < 0) and (self.nenner < 0):
            return "("+str(self.zaehler * -1) + "/" + str(self.nenner * -1) + ")"
        elif self.nenner == 1:
            return "("+str(self.zaehler) + ")"
        return "("+str(self.zaehler) + "/" + str(self.nenner) + ")"

    def __add__(self, other):
        """
        Nimmt zwei Brüche entgegen und addiert diese
        :param other: Der Bruch mit dem addiert werden soll.
        :return: Gibt den addierten Bruch zurück
        """
        if type(other) == Bruch:
            return Bruch((self.zaehler*other.nenner + other.zaehler*self.nenner),(self.nenner*other.nenner))
        elif type(other) == int:
            return Bruch((self.zaehler+other*self.nenner),self.nenner)
        else:
            raise TypeError

    def __iadd__(self, other):
        """
        Inkrementale addition für Brüche: +=
        :param other: Siehe __add__()
        :return: Rückgabe von __add__()
        """
        return self.__add__(other)

    def __radd__(self, other):
        """
        int + Bruch
        :param other: Siehe __add__()
        :return: Rückgabe von __add__()
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Nimmt zwei Brüche entgegen und subtrahiert diese
        :param other: Der Bruch der subtrahiert werden soll
        :return: Gibt die Differenz der beiden Brüche zurück
        """
        if type(other) == Bruch:
            return Bruch((self.zaehler*other.nenner - other.zaehler*self.nenner),(self.nenner*other.nenner))
        elif type(other) == int:
            return Bruch((self.zaehler-other*self.nenner),self.nenner)
        else:
            raise TypeError

    def __isub__(self, other):
        """
        Inkrementele Subtraktion von Brüchen
        :param other: Siehe __sub__()
        :return: Rückgabe von __sub__()
        """
        return self.__sub__(other)

    def __rsub__(self, other):
        """
        int - Bruch
        :param other:
        :return:
        """
        other= Bruch(other)
        return other.__sub__(self)

    def __truediv__(self, other):
        """
        Nimmt wei Brüche entgegen und dividiert diese
        :param other: Der zweite Bruch mit dem dividiert wird
        :return: Gibt das Ergebnis der Dvision der beiden Brüche zurück
        """
        if type(other) == int:
            if self == 0:
                raise ZeroDivisionError
            ergebnis = float(self)*float(1/other)
            return float(ergebnis)
        elif type(other) == Bruch:
            return float(self) * float(~other)
        else:
            raise TypeError

    def __itruediv__(self, other):
        """
        Inkrementele division von Brüchen
        :param other: Siehe __truediv__()
        :return: Rückgabe von __truediv()
        """
        return self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        int / Bruch
        :param other: Siehe __truediv()
        :return: Rückgabe von __truediv()
        """
        return self.__truediv__(other)

    def __mul__(self, other):
        """
        Nimmt zwei Brüche entgegen und multipliziert diese miteinander
        :param other: Der zweite Bruch mit dem multipliziert werden soll
        :return: Gibt das Ergebnis der Multiplikation der beiden Brüche zurück
        """
        if type(other) == int:
            if self == 0:
                raise ZeroDivisionError
            ergebnis = float(self)*float(other)
            return float(ergebnis)
        elif type(other) == Bruch:
            return float(self) * float(other)
        else:
            raise TypeError

    def __imul__(self, other):
        """
        Inkrementele multiplikation von Brüchen
        :param other: Siehe __mul__()
        :return: Rückgabe von __mul__()
        """
        return self.__mul__(other)

    def __rmul__(self, other):
        """
        int * Bruch
        :param other: Siehe __mul__()
        :return: Rückgabe von __mul__()
        """
        return self.__mul__(other)

    def __ge__(self, other):
        """
        Überprüft ob ein Bruch >= ein anderer Bruch ist.
        :param other: Der zweite Bruch
        :return: Gibt True,wenn der Bruch größer oder gleich ist, oder False zurück
        """
        return float(self)>=float(other)

    def __gt__(self, other):
        """
        Überprüft ob ein Bruch > als ein andere Bruch ist
        :param other: Der zweite Bruch
        :return: Gibt True,wenn der Bruch größer ist, oder False zurück
        """
        return float(self)>float(other)

    def __le__(self, other):
        """
        Überprüft ob ein Bruch <= einen anderen Bruch ist
        :param other: Der zweite Bruch
        :return: Gibt True,wenn der Bruch kleiner oder gleich ist, oder False zurück
        """
        return float(self)<=float(other)

    def __lt__(self, other):
        """
        Überprüft ob ein Bruch < als ein anderer Bruch ist
        :param other: Der zweite Bruch
        :return: Gibt True,wenn der Bruch kleiner ist, oder False zurück
        """
        return float(self)<float(other)

    def __iter__(self):
        """
        Iteriert durch den Bruch
        :return:Iterator von tuple: (Zaehler, Nenner)
        """
        return (self.zaehler, self.nenner).__iter__()

