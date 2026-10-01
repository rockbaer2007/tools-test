# UGSo Tools Test

Referenzpaket für die deklarative Tool-Schnittstelle 0.1 von [HA Grafik Visual Studio](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio). Das Paket enthält **Test-Seitenfarbe** mit Vorschau und bestätigter Änderung der Seitenhintergrundfarbe. Es führt keinen eigenen Code aus. Das getrennte [Widget-Test-Repository](https://github.com/rockbaer2007/widget-test) prüft die Widget-Schnittstelle.

## Funktionstest

1. Lade `tools-test-0.1.0.tp.zip` aus dem [Release v0.1.0](https://github.com/rockbaer2007/tools-test/releases/tag/v0.1.0) herunter oder erstelle es mit `python build.py` neu.
2. Installiere die Datei unter **Einstellungen → Tools** im Studio.
3. Öffne **Test-Seitenfarbe** mit **Ausführen**. Die Vorschau darf das Projekt noch nicht ändern. Wähle eine Farbe und bestätige mit **Anwenden**.
4. Prüfe die Seitenfarbe im Editor und teste **Rückgängig**. Danach kann das Paket im Tool-Tab wieder entfernt werden.

Quelle: `package/manifest.json` und `package/icons/tools-test.svg`. `dist/` enthält die fertige Testdatei. Der aktuelle Importer nimmt `.tp.zip` an; die spätere Endung `.tp` ist noch nicht implementiert. Weitere Regeln stehen in der [Tool-Schnittstellenbeschreibung](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/tool-rules.md).

## English

This is a reference package for HA Grafik Visual Studio's declarative tool API 0.1. Download `tools-test-0.1.0.tp.zip` from [release v0.1.0](https://github.com/rockbaer2007/tools-test/releases/tag/v0.1.0), or rebuild it with `python build.py`. Install it under **Settings → Tools**. Run **Test-Seitenfarbe**, inspect its preview, then apply a chosen color. Verify the page background and **Undo**. The current importer accepts `.tp.zip`; `.tp` is planned for a later version.
