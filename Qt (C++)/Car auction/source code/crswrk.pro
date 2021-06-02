QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    adddialog.cpp \
    chartdialog.cpp \
    deletequestion.cpp \
    info.cpp \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    adddialog.h \
    chartdialog.h \
    deletequestion.h \
    info.h \
    mainwindow.h

FORMS += \
    adddialog.ui \
    chartdialog.ui \
    deletequestion.ui \
    info.ui \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target


win32: {
    VERSION = 1.0.0
    QMAKE_TARGET_COMPANY = mxkmn
    QMAKE_TARGET_PRODUCT = Car auction
    QMAKE_TARGET_DESCRIPTION = Course work
    QMAKE_TARGET_COPYRIGHT = Yarkov Max
    RC_ICONS += logo.ico
}

DISTFILES +=

RESOURCES += \
    icon.qrc
