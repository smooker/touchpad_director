TEMPLATE = app
TARGET = uinput

INCLUDEPATH += .

QMAKE_CXXFLAGS += -O2 -msse -msse2 -std=c++11 -fopenmp -DMAGICKCORE_QUANTUM_DEPTH=16 -DMAGICKCORE_HDRI_ENABLE=0
QMAKE_CFLAGS += -O2 -msse -msse2 -std=c++11 -fopenmp -DMAGICKCORE_QUANTUM_DEPTH=16 -DMAGICKCORE_HDRI_ENABLE=0

SOURCES += uinput-sample.c

