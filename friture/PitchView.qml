import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Layouts 1.15
import Friture 1.0

Item {
    id: pitch_view

    property var stateId

    signal pointSelected(real x, real y)

    // delay the load of Plot until stateId is set
    onStateIdChanged: {
        loader.sourceComponent = viewComponent
    }

    Loader {
        id: loader
        anchors.fill: parent
    }

    Component {
        id: viewComponent
        RowLayout {
            anchors.fill: parent

            Scope {
                id: scope
                stateId: pitch_view.stateId
                // implicitWidth: 300

                Layout.fillWidth: true
                Layout.fillHeight: true


                onPointSelected: (x, y) => pitch_view.pointSelected(x, y)
            }

            ColumnLayout {
                id: pitchCol
                spacing: 0
                Layout.alignment: Qt.AlignTop | Qt.AlignLeft

                property var pitchModel: Store.dock_states[pitch_view.stateId]

                FontMetrics {
                    id: fontMetrics
                    font.pointSize: 14
                    font.bold: true
                }

                Text {
                    id: note
                    text: pitchCol.pitchModel.note
                    textFormat: Text.PlainText
                    font.pointSize: 14
                    font.bold: true
                    rightPadding: 6
                    horizontalAlignment: Text.AlignRight
                    Layout.alignment: Qt.AlignTop | Qt.AlignRight
                }

                Text {
                    id: pitchHz
                    text: pitchCol.pitchModel.pitch
                    textFormat: Text.PlainText
                    font.pointSize: 14
                    font.bold: true
                    rightPadding: 6
                    horizontalAlignment: Text.AlignRight
                    Layout.preferredWidth: fontMetrics.boundingRect("000.0").width
                    Layout.alignment: Qt.AlignTop | Qt.AlignRight
                }

                Text {
                    id: pitchUnit
                    text: pitchCol.pitchModel.pitch_unit
                    textFormat: Text.PlainText
                    rightPadding: 6
                    horizontalAlignment: Text.AlignRight
                    Layout.alignment: Qt.AlignTop | Qt.AlignRight
                }
            }
        }
    }
}
