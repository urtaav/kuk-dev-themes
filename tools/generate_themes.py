# La plataforma solo carga editorScheme como archivo si termina en .xml.
"""Genera los .theme.json y esquemas .xml de Kuk y sus variantes con las mismas claves.

Uso: python tools/generate_themes.py src/main/resources
"""
import json
import sys
from pathlib import Path

OUT = Path(sys.argv[1])


def hx(c):
    return c.lstrip("#").upper()


def mix(a, b, t):
    """Mezcla a hacia b en proporción t."""
    a, b = hx(a), hx(b)
    ra = [int(a[i:i + 2], 16) for i in (0, 2, 4)]
    rb = [int(b[i:i + 2], 16) for i in (0, 2, 4)]
    return "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(ra, rb))


# Kuk: carbón #151517 en todo, gutter más oscuro, acento lima. Medido de las referencias.
# selectionText es el texto sobre la selección de listas/árbol (oscuro cuando la selección es lima).
THEMES = {
    "Kuk": dict(
        ui=dict(stripe="151517", chrome="151517", bg="151517", editor="151517", gutter="101012",
                panel="18181B", raised="1E1D22", hover="1E1D22", selection="1E1D22", selectionText="FFFFFF",
                selectionInactive="1A1A1D", chip="1E1D22", border="0F0F11", accent="DCFB58", onAccent="151517", rowHover="1E1D22",
                text="EFEEF2", textBright="FFFFFF", muted="5A595E", disabled="3A393D", thumb="2A2A2E",
                thumbHover="3A3A3F", lineNumber="3A3A3E", lineNumberActive="DCFB58",
                error="F7584B", warning="F5C451", success="DCFB58"),
        syntax=dict(keyword="93C6E8", string="F5EDB0", number="AB87D1", constant="AB87D1",
                    function="F3E9A0", functionCall="AB87D1", ident="E8E8EC", punct="E8E8EC", operator="FFFFFF",
                    brace="AB87D1", klass="DDF39A", interface="DDF39A", field="B9D4E8", tag="93C6E8",
                    attribute="DDF39A", annotation="DCFB58", escape="DCFB58", comment="55545A", doc="6A6970"),
        caret="DCFB58", keywordFont=0),
    # Variante Neon: gris neutro, fila seleccionada en lima con texto oscuro, keywords rosas.
    "Kuk Neon": dict(
        ui=dict(stripe="1A1A1A", chrome="1F1F1F", bg="222222", editor="1F1F1F", gutter="1F1F1F",
                panel="262626", raised="2A2A2A", hover="2C2C2C", selection="B8F23A", selectionText="101010",
                selectionInactive="2E2E2E", chip="2E2E2E", border="2A2A2A", accent="B8F23A", onAccent="101010", rowHover="B8F23A1F",
                text="E6E6E6", textBright="FFFFFF", muted="8A8A8A", disabled="555555", thumb="3A3A3A",
                thumbHover="4A4A4A", lineNumber="5A5A5A", lineNumberActive="B8F23A",
                error="FF5F6D", warning="F2C14E", success="B8F23A"),
        syntax=dict(keyword="E87FA6", string="E8A06E", number="F0D58C", constant="F0D58C",
                    function="C6E86A", functionCall="C6E86A", ident="F2F2F2", punct="D8D8D8", operator="D8D8D8",
                    brace="D8D8D8", klass="E8E06A", interface="E8E06A", field="D5E694", tag="E87FA6",
                    attribute="D5E694", annotation="E6E6E6", escape="E8A06E", comment="6A6A6A", doc="7A7A7A"),
        caret="B8F23A", keywordFont=0),
    # Variante roja/rosa: misma base carbón que Kuk, selección rosa con texto e iconos oscuros.
    "Kuk Ember": dict(
        ui=dict(stripe="151517", chrome="151517", bg="151517", editor="151517", gutter="101012",
                panel="18181B", raised="1E1D22", hover="1E1D22", selection="FF5C8A", selectionText="151517",
                selectionInactive="2A1C22", chip="1E1D22", border="0F0F11", accent="FF5C8A", onAccent="151517",
                rowHover="FF5C8A1F", text="EFEEF2", textBright="FFFFFF", muted="5E5A60", disabled="3A393D",
                thumb="2A2A2E", thumbHover="3A3A3F", lineNumber="3A3A3E", lineNumberActive="FF5C8A",
                error="FF4D5E", warning="F5C451", success="7FD88F"),
        syntax=dict(keyword="FF7A9A", string="F6D6A8", number="FF9F7A", constant="FF9F7A",
                    function="FFD1DC", functionCall="C9A0F0", ident="ECEAEE", punct="ECEAEE", operator="FFFFFF",
                    brace="C9A0F0", klass="FFC9B5", interface="FFC9B5", field="F2B8C6", tag="FF7A9A",
                    attribute="FFC9B5", annotation="FF5C8A", escape="FF5C8A", comment="5A555B", doc="6E686F"),
        caret="FF5C8A", keywordFont=0),
    # Variante azul: misma base carbón, selección azul con texto e iconos oscuros, números cálidos de contraste.
    "Kuk Abyss": dict(
        ui=dict(stripe="151517", chrome="151517", bg="151517", editor="151517", gutter="101012",
                panel="18181B", raised="1E1D22", hover="1E1D22", selection="5AB0FF", selectionText="151517",
                selectionInactive="1A2230", chip="1E1D22", border="0F0F11", accent="5AB0FF", onAccent="151517",
                rowHover="5AB0FF1F", text="EFEEF2", textBright="FFFFFF", muted="5A5D64", disabled="3A3B40",
                thumb="2A2A2E", thumbHover="3A3A3F", lineNumber="3A3B40", lineNumberActive="5AB0FF",
                error="FF5F6D", warning="FFB86B", success="7FD8B5"),
        syntax=dict(keyword="7AB8FF", string="A8E0D8", number="FFB86B", constant="FFB86B",
                    function="D6E4FF", functionCall="B79CFF", ident="E8EAF0", punct="E8EAF0", operator="FFFFFF",
                    brace="B79CFF", klass="9EE6FF", interface="9EE6FF", field="9FC4E8", tag="7AB8FF",
                    attribute="9EE6FF", annotation="5AB0FF", escape="5AB0FF", comment="525660", doc="666B76"),
        caret="5AB0FF", keywordFont=0),
    # Ámbar sobre negro cálido: modo noche acogedor, poca luz azul.
    "Kuk Amber": dict(
        ui=dict(stripe="17140F", chrome="17140F", bg="17140F", editor="17140F", gutter="120F0B",
                panel="1C1813", raised="231E17", hover="231E17", selection="FFB547", selectionText="17140F",
                selectionInactive="2E2518", chip="231E17", border="100D09", accent="FFB547", onAccent="17140F",
                rowHover="FFB5471F", text="F2E9DC", textBright="FFFFFF", muted="6E6457", disabled="4A4238",
                thumb="2E281F", thumbHover="3E362A", lineNumber="3E362C", lineNumberActive="FFB547",
                error="FF6B5B", warning="FFB547", success="A8D672"),
        syntax=dict(keyword="FF9E5E", string="C8E08A", number="9CD8F0", constant="9CD8F0",
                    function="FFE8B8", functionCall="F7A6C8", ident="EDE4D6", punct="D9CFC0", operator="FFB547",
                    brace="F7A6C8", klass="FFD58A", interface="FFD58A", field="F2C6A0", tag="FF9E5E",
                    attribute="FFD58A", annotation="FFB547", escape="FFB547", comment="6B6052", doc="857A6A"),
        caret="FFB547", keywordFont=0),
    # Índigo profundo con lavanda, rosa y aqua: el más llamativo en capturas.
    "Kuk Nebula": dict(
        ui=dict(stripe="13111C", chrome="13111C", bg="13111C", editor="13111C", gutter="0F0D17",
                panel="171422", raised="1F1B30", hover="1F1B30", selection="B18CFF", selectionText="13111C",
                selectionInactive="261F3D", chip="1F1B30", border="0E0C16", accent="B18CFF", onAccent="13111C",
                rowHover="B18CFF1F", text="ECE8FA", textBright="FFFFFF", muted="625C7A", disabled="3F3A54",
                thumb="2A2540", thumbHover="3A3456", lineNumber="3A3552", lineNumberActive="B18CFF",
                error="FF6B9A", warning="FFC36B", success="6BF2C4"),
        syntax=dict(keyword="F48FD8", string="F9C784", number="FF9E7A", constant="FF9E7A",
                    function="C9B6FF", functionCall="8FD8FF", ident="E9E5F7", punct="C9C2E0", operator="F48FD8",
                    brace="8FD8FF", klass="7DF3E1", interface="7DF3E1", field="D1C4FF", tag="F48FD8",
                    attribute="7DF3E1", annotation="B18CFF", escape="B18CFF", comment="5E587A", doc="726B90"),
        caret="B18CFF", keywordFont=0),
    # Negro verdoso con jade: calma y foco.
    "Kuk Jade": dict(
        ui=dict(stripe="0F1513", chrome="0F1513", bg="0F1513", editor="0F1513", gutter="0B100E",
                panel="131A17", raised="18211D", hover="18211D", selection="34E0A1", selectionText="0F1513",
                selectionInactive="1C2B25", chip="18211D", border="0A0F0D", accent="34E0A1", onAccent="0F1513",
                rowHover="34E0A11F", text="E3F2EC", textBright="FFFFFF", muted="587068", disabled="37463F",
                thumb="22302A", thumbHover="2F4038", lineNumber="2F3F38", lineNumberActive="34E0A1",
                error="FF6F7D", warning="F2C76B", success="34E0A1"),
        syntax=dict(keyword="6CCBFF", string="F2D49B", number="FF9F8A", constant="FF9F8A",
                    function="9EF0C9", functionCall="C3A6FF", ident="E0EEE8", punct="C2D4CC", operator="34E0A1",
                    brace="C3A6FF", klass="B8F5D4", interface="B8F5D4", field="A9D9C6", tag="6CCBFF",
                    attribute="B8F5D4", annotation="34E0A1", escape="34E0A1", comment="4E6359", doc="627A70"),
        caret="34E0A1", keywordFont=0),
    # Tema claro: papel cálido, tinta oscura y acento terracota.
    "Kuk Dawn": dict(
        dark=False,
        ui=dict(stripe="EFE9DF", chrome="EFE9DF", bg="F4EFE7", editor="FBF8F3", gutter="F4EFE7",
                panel="FFFFFF", raised="EAE3D7", hover="E9E2D6", selection="D9573B", selectionText="FFFFFF",
                selectionInactive="E6DFD2", chip="E2DACB", border="E2DACB", accent="D9573B", onAccent="FFFFFF",
                rowHover="D9573B1A", text="2B2620", textBright="14110D", muted="8A8174", disabled="B8AFA2",
                thumb="D3CBBE", thumbHover="BFB6A8", lineNumber="C2B9AC", lineNumberActive="D9573B",
                caretRow="F3EDE3", error="D63B3B", warning="B7791F", success="3F8F5A"),
        syntax=dict(keyword="B2366B", string="4E7D2A", number="C2501F", constant="C2501F",
                    function="1D5FA6", functionCall="7A3EA8", ident="2B2620", punct="5A5248", operator="B2366B",
                    brace="7A3EA8", klass="2F6F8F", interface="2F6F8F", field="9B4F7A", tag="B2366B",
                    attribute="2F6F8F", annotation="D9573B", escape="C2501F", comment="9C9284", doc="8C8272"),
        caret="D9573B", keywordFont=0),
    # Paleta 1 del autor: pizarra monocroma #21262B / #A9A9A9 / #F1F1F1 / #778898.
    "Kuk Slate": dict(
        ui=dict(stripe="1C2025", chrome="1C2025", bg="21262B", editor="21262B", gutter="1D2126",
                panel="262C32", raised="2B3238", hover="2B3238", selection="778898", selectionText="F1F1F1",
                selectionInactive="2E363E", chip="2B3238", border="1A1E22", accent="778898", onAccent="F1F1F1",
                accentText="9AA9B9", rowHover="7788982E", text="F1F1F1", textBright="FFFFFF", muted="A9A9A9",
                disabled="5A626B", thumb="353D45", thumbHover="46505A", lineNumber="4E5862",
                lineNumberActive="F1F1F1", error="E07A7A", warning="D9B97A", success="8FBF9A"),
        syntax=dict(keyword="9AA9B9", string="A9A9A9", number="B8C4D0", constant="B8C4D0",
                    function="DDE3E9", functionCall="C6CED6", ident="D6D6D6", punct="A9A9A9", operator="9AA9B9",
                    brace="A9A9A9", klass="F1F1F1", interface="F1F1F1", field="C6CED6", tag="9AA9B9",
                    attribute="A9A9A9", annotation="9AA9B9", escape="DDE3E9", comment="6B7682", doc="7D8894"),
        caret="F1F1F1", keywordFont=1),
    # Paleta 2 del autor: claro #F7F7F7 / #373634 / #DCEB7D / #EEF3E1 / #000000.
    # El lima es fondo (selección, botón, subrayado); como texto se usa oliva oscuro legible.
    "Kuk Matcha": dict(
        dark=False,
        ui=dict(stripe="E6ECD6", chrome="EEF3E1", bg="EEF3E1", editor="F7F7F7", gutter="F7F7F7",
                panel="FFFFFF", raised="EEF3E1", hover="E6ECD6", selection="DCEB7D", selectionText="000000",
                selectionInactive="E6ECD6", chip="DCEB7D", border="E2E6D8", accent="DCEB7D", onAccent="000000",
                accentText="5F6F12", rowHover="DCEB7D66", editorSelection="DCEB7D", caretRow="EEF3E1",
                text="373634", textBright="000000", muted="8A8984", disabled="B5B4AE", thumb="D5D9CC",
                thumbHover="C2C7B8", lineNumber="B8B7B1", lineNumberActive="000000",
                error="C93A3A", warning="A86F12", success="5E7F1A"),
        syntax=dict(keyword="000000", string="5F6F12", number="8C7A12", constant="8C7A12",
                    function="000000", functionCall="373634", ident="373634", punct="5A5955", operator="000000",
                    brace="5A5955", klass="000000", interface="000000", field="55544F", tag="000000",
                    attribute="5F6F12", annotation="5F6F12", escape="5F6F12", comment="9A9993", doc="8A8984"),
        caret="000000", keywordFont=1),
}

# Clave UI -> rol de la paleta. "*" cubre todo componente sin clave explícita.
UI_KEYS = {
    "*": {
        "background": "bg", "foreground": "text", "infoForeground": "muted",
        "selectionBackground": "selection", "selectionForeground": "selectionText",
        "selectionInactiveBackground": "selectionInactive", "selectionBackgroundInactive": "selectionInactive",
        "disabledForeground": "disabled", "inactiveForeground": "muted",
        "borderColor": "border", "separatorColor": "border", "lineSeparatorColor": "border",
        "hoverBackground": "hover", "focusColor": "accent", "focusedBorderColor": "accent",
    },
    "ActionButton.hoverBackground": "hover", "ActionButton.hoverBorderColor": "hover",
    "ActionButton.pressedBackground": "selection", "ActionButton.pressedBorderColor": "selection",
    "Borders.color": "border", "Borders.ContrastBorderColor": "border",
    "Button.background": "raised", "Button.foreground": "text",
    "Button.startBorderColor": "border", "Button.endBorderColor": "border", "Button.focusedBorderColor": "accent",
    "Button.default.startBackground": "accent", "Button.default.endBackground": "accent",
    "Button.default.foreground": "onAccent", "Button.default.startBorderColor": "accent",
    "Button.default.endBorderColor": "accent", "Button.default.focusedBorderColor": "accent",
    "Button.default.focusColor": "accent",
    "ComboBox.background": "panel", "ComboBox.nonEditableBackground": "panel",
    "ComboBox.ArrowButton.background": "panel", "ComboBox.ArrowButton.nonEditableBackground": "panel",
    "ComboBox.selectionBackground": "selection", "ComboBoxButton.background": "panel",
    "CompletionPopup.background": "panel", "CompletionPopup.selectionBackground": "selection",
    "CompletionPopup.selectionInactiveBackground": "selectionInactive", "CompletionPopup.matchForeground": "accentText",
    "Component.borderColor": "border", "Component.disabledBorderColor": "border",
    "Component.focusColor": "accent", "Component.focusedBorderColor": "accent",
    "Component.iconColor": "muted", "Component.hoverIconColor": "text",
    "Component.errorFocusColor": "error", "Component.inactiveErrorFocusColor": "error",
    "Component.warningFocusColor": "warning", "Component.inactiveWarningFocusColor": "warning",
    "Counter.background": "accent", "Counter.foreground": "onAccent",
    "DefaultTabs.background": "bg", "DefaultTabs.borderColor": "border", "DefaultTabs.hoverBackground": "hover",
    "DefaultTabs.underlineColor": "accent", "DefaultTabs.inactiveUnderlineColor": "muted",
    "DefaultTabs.underlinedTabBackground": "raised", "DefaultTabs.underlinedTabForeground": "textBright",
    "DragAndDrop.areaBackground": "selection",
    "Editor.background": "editor", "Editor.foreground": "text", "Editor.shortcutForeground": "accentText",
    "Editor.SearchField.background": "panel", "Editor.Toolbar.borderColor": "border",
    "EditorPane.background": "editor",
    "EditorTabs.background": "chrome", "EditorTabs.borderColor": "border", "EditorTabs.hoverBackground": "hover",
    "EditorTabs.selectedBackground": "editor", "EditorTabs.inactiveColoredFileBackground": "editor",
    "EditorTabs.underlineColor": "accent", "EditorTabs.inactiveUnderlineColor": "muted",
    "EditorTabs.underlinedTabBackground": "raised", "EditorTabs.underlinedTabForeground": "textBright",
    "GotItTooltip.background": "raised", "GotItTooltip.foreground": "text", "GotItTooltip.borderColor": "border",
    "Group.separatorColor": "border",
    "InplaceRefactoringPopup.background": "panel", "InplaceRefactoringPopup.borderColor": "border",
    "Label.foreground": "text", "Label.disabledForeground": "disabled", "Label.infoForeground": "muted",
    "Link.activeForeground": "accentText", "Link.hoverForeground": "accentText",
    "Link.pressedForeground": "accentText", "Link.visitedForeground": "accentText",
    "List.background": "bg", "List.hoverBackground": "rowHover", "List.selectionBackground": "selection",
    "List.selectionInactiveBackground": "selectionInactive", "List.selectionForeground": "selectionText",
    "MainMenu.background": "chrome", "MainMenu.foreground": "text", "MainMenu.selectionBackground": "selection",
    "MainToolbar.background": "chrome", "MainToolbar.inactiveBackground": "chrome", "MainToolbar.foreground": "text",
    "MainToolbar.Dropdown.hoverBackground": "hover", "MainToolbar.Dropdown.pressedBackground": "selection",
    "MainToolbar.Icon.hoverBackground": "hover", "MainToolbar.Icon.pressedBackground": "selection",
    "MainWindow.background": "chrome",
    "Menu.background": "panel", "Menu.foreground": "text", "Menu.borderColor": "border",
    "Menu.separatorColor": "border", "Menu.selectionBackground": "selection",
    "MenuBar.background": "chrome", "MenuBar.borderColor": "border",
    "MenuItem.background": "panel", "MenuItem.selectionBackground": "selection", "MenuItem.acceleratorForeground": "muted",
    "NavBar.borderColor": "border",
    "Notification.background": "panel", "Notification.foreground": "text", "Notification.borderColor": "border",
    "NotificationsToolwindow.newNotification.background": "raised",
    "NotificationsToolwindow.Notification.hoverBackground": "hover",
    "Panel.background": "bg",
    "ParameterInfo.background": "panel", "ParameterInfo.foreground": "text",
    "ParameterInfo.borderColor": "border", "ParameterInfo.currentParameterForeground": "accentText",
    "PasswordField.background": "panel",
    "Plugins.background": "bg", "Plugins.SearchField.background": "panel", "Plugins.SectionHeader.background": "bg",
    "Plugins.lightSelectionBackground": "selection", "Plugins.hoverBackground": "hover",
    "Plugins.Tab.selectedBackground": "selection", "Plugins.Tab.hoverBackground": "hover",
    "Popup.background": "panel", "Popup.borderColor": "border", "Popup.inactiveBorderColor": "border",
    "Popup.separatorColor": "border", "Popup.Header.activeBackground": "panel",
    "Popup.Header.inactiveBackground": "panel", "Popup.Advertiser.background": "panel",
    "Popup.Advertiser.foreground": "muted", "Popup.Toolbar.background": "panel", "Popup.Toolbar.borderColor": "border",
    "PopupMenu.background": "panel", "PopupMenu.selectionBackground": "selection",
    "ProgressBar.trackColor": "raised", "ProgressBar.progressColor": "accent",
    "ProgressBar.indeterminateStartColor": "accent", "ProgressBar.indeterminateEndColor": "raised",
    "RunWidget.background": "raised", "RunWidget.foreground": "text",
    "RunWidget.hoverBackground": "hover", "RunWidget.pressedBackground": "selection",
    "ScrollBar.background": "bg", "ScrollBar.trackColor": "bg",
    "ScrollBar.thumbColor": "thumb", "ScrollBar.thumbBorderColor": "thumb",
    "ScrollBar.hoverThumbColor": "thumbHover", "ScrollBar.hoverThumbBorderColor": "thumbHover",
    "ScrollBar.Transparent.thumbColor": "thumb", "ScrollBar.Transparent.thumbBorderColor": "thumb",
    "ScrollBar.Transparent.hoverThumbColor": "thumbHover", "ScrollBar.Transparent.hoverThumbBorderColor": "thumbHover",
    "ScrollBar.Mac.thumbColor": "thumb", "ScrollBar.Mac.thumbBorderColor": "thumb",
    "ScrollBar.Mac.hoverThumbColor": "thumbHover", "ScrollBar.Mac.hoverThumbBorderColor": "thumbHover",
    "ScrollBar.Mac.Transparent.thumbColor": "thumb", "ScrollBar.Mac.Transparent.thumbBorderColor": "thumb",
    "ScrollBar.Mac.Transparent.hoverThumbColor": "thumbHover",
    "ScrollBar.Mac.Transparent.hoverThumbBorderColor": "thumbHover",
    "ScrollPane.background": "bg",
    "SearchEverywhere.Header.background": "panel", "SearchEverywhere.SearchField.background": "panel",
    "SearchEverywhere.SearchField.borderColor": "border", "SearchEverywhere.Tab.selectedBackground": "selection",
    "SearchEverywhere.List.separatorColor": "border", "SearchEverywhere.Advertiser.background": "panel",
    "SearchEverywhere.Advertiser.foreground": "muted",
    "Separator.separatorColor": "border",
    "SidePanel.background": "bg",
    "SpeedSearch.background": "raised", "SpeedSearch.foreground": "text",
    "SpeedSearch.borderColor": "border", "SpeedSearch.errorForeground": "error",
    "StatusBar.background": "chrome", "StatusBar.borderColor": "border", "StatusBar.hoverBackground": "hover",
    "StatusBar.Widget.hoverBackground": "hover", "StatusBar.Widget.pressedBackground": "selection",
    "StatusBar.Breadcrumbs.foreground": "muted", "StatusBar.Breadcrumbs.hoverBackground": "hover",
    "StatusBar.Breadcrumbs.selectionBackground": "selection", "StatusBar.Breadcrumbs.floatingBackground": "panel",
    "TabbedPane.background": "bg", "TabbedPane.contentAreaColor": "bg", "TabbedPane.hoverColor": "hover",
    "TabbedPane.focusColor": "raised", "TabbedPane.underlineColor": "accent", "TabbedPane.disabledUnderlineColor": "muted",
    "Table.background": "bg", "Table.stripeColor": "panel", "Table.gridColor": "border",
    "Table.hoverBackground": "rowHover", "Table.selectionBackground": "selection",
    "Table.selectionInactiveBackground": "selectionInactive",
    "TableHeader.background": "panel", "TableHeader.bottomSeparatorColor": "border", "TableHeader.separatorColor": "border",
    "TextArea.background": "bg", "TextField.background": "panel", "TextPane.background": "bg",
    "TitlePane.background": "chrome", "TitlePane.inactiveBackground": "chrome", "TitlePane.Button.hoverBackground": "hover",
    "ToggleButton.onBackground": "accent", "ToggleButton.onForeground": "onAccent",
    "ToggleButton.offBackground": "raised", "ToggleButton.buttonColor": "text",
    "Toolbar.Floating.background": "panel",
    "ToolTip.background": "raised", "ToolTip.foreground": "text", "ToolTip.borderColor": "border",
    "ToolTip.infoForeground": "muted", "ToolTip.Actions.background": "panel",
    "ToolWindow.background": "bg",
    "ToolWindow.Header.background": "bg", "ToolWindow.Header.inactiveBackground": "bg",
    "ToolWindow.Header.borderColor": "border", "ToolWindow.HeaderCloseButton.background": "bg",
    "ToolWindow.HeaderTab.hoverBackground": "hover", "ToolWindow.HeaderTab.hoverInactiveBackground": "hover",
    "ToolWindow.HeaderTab.selectedInactiveBackground": "selectionInactive",
    "ToolWindow.HeaderTab.underlineColor": "accent", "ToolWindow.HeaderTab.inactiveUnderlineColor": "muted",
    "ToolWindow.HeaderTab.underlinedTabBackground": "raised", "ToolWindow.HeaderTab.underlinedTabInactiveBackground": "bg",
    "ToolWindow.Button.hoverBackground": "hover", "ToolWindow.Button.selectedBackground": "chip",
    "ToolWindow.Button.selectedForeground": "textBright",
    "ToolWindow.Stripe.background": "stripe", "ToolWindow.Stripe.borderColor": "border",
    "Tree.background": "bg", "Tree.hoverBackground": "rowHover", "Tree.selectionBackground": "selection",
    "Tree.selectionInactiveBackground": "selectionInactive", "Tree.selectionForeground": "selectionText",
    "Tree.modifiedItemForeground": "accentText",
    "ValidationTooltip.errorBackground": "panel", "ValidationTooltip.errorBorderColor": "error",
    "ValidationTooltip.warningBackground": "panel", "ValidationTooltip.warningBorderColor": "warning",
    "VersionControl.Log.Commit.currentBranchBackground": "raised", "VersionControl.Log.Commit.hoveredBackground": "hover",
    "Viewport.background": "bg",
    "WelcomeScreen.background": "bg", "WelcomeScreen.Details.background": "bg", "WelcomeScreen.separatorColor": "border",
    "WelcomeScreen.SidePanel.background": "panel", "WelcomeScreen.Projects.background": "bg",
    "WelcomeScreen.Projects.selectionBackground": "selection",
    "WelcomeScreen.Projects.selectionInactiveBackground": "selectionInactive",
}


def ref(role):
    return "kuk" + role[0].upper() + role[1:]


# Hex exclusivos de la carpeta para poder recolorearla al seleccionar (iconColorsOnSelection).
FOLDER_FILL = {True: "EEEEF1", False: "6E6559"}
FOLDER_ICON = {True: "/kuk/folder.svg", False: "/kuk/folder-light.svg"}


def folder_svg(fill):
    return f"""<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 3.5C1 2.67 1.67 2 2.5 2H6.1c.4 0 .78.16 1.06.44L8.7 4H13.5c.83 0 1.5.67 1.5 1.5v7c0 .83-.67 1.5-1.5 1.5h-11C1.67 14 1 13.33 1 12.5v-9Z" fill="#{fill}"/>
</svg>
"""


def theme_json(name, t, scheme_file):
    ui = {}
    for key, role in UI_KEYS.items():
        ui[key] = {k: ref(r) for k, r in role.items()} if isinstance(role, dict) else ref(role)
    # Sin máscara para que las pestañas inactivas no se vean grisáceas.
    ui["EditorTabs.inactiveMaskColor"] = "#00000000"
    dark = t.get("dark", True)
    t["ui"].setdefault("accentText", t["ui"]["accent"])
    on_selection = {"#" + FOLDER_FILL[dark]: "#" + t["ui"]["selectionText"]}
    if t["ui"]["selection"] == t["ui"]["accent"]:
        # Selección de color: los iconos de la New UI toman el color del texto seleccionado.
        stroke, fill = ("#CED0D6", "#43454A") if dark else ("#6C707E", "#EBECF0")
        on_selection.update({stroke: "#" + t["ui"]["selectionText"], fill: "#" + t["ui"]["selection"]})
    # Sin rayas de indentación en árboles (Project, dependencias); ClassicPainter las pinta con Tree.hash.
    ui["Tree.paintLines"] = False
    ui["Tree.hash"] = "#00000000"
    ui["SearchMatch.startBackground"] = "#" + t["ui"]["accent"] + "66"
    ui["SearchMatch.endBackground"] = "#" + t["ui"]["accent"] + "66"
    return {
        "name": name,
        "author": "NYX Devs",
        "dark": dark,
        "editorScheme": "/" + scheme_file,
        "colors": {ref(k): "#" + v for k, v in t["ui"].items()},
        "ui": ui,
        "icons": {
            "ColorPalette": {"Actions.Green": "#" + t["ui"]["accent"], "Objects.Green": "#" + t["ui"]["accent"]},
            # Carpeta sólida clara en lugar del contorno gris de la New UI.
            "/expui/nodes/folder.svg": FOLDER_ICON[dark],
            "/nodes/folder.svg": FOLDER_ICON[dark],
        },
        "iconColorsOnSelection": on_selection,
    }


def attr(name, fg=None, bg=None, font=None, effect=None, effect_type=None, stripe=None):
    opts = [("FOREGROUND", fg), ("BACKGROUND", bg), ("FONT_TYPE", font),
            ("EFFECT_COLOR", effect), ("EFFECT_TYPE", effect_type), ("ERROR_STRIPE_COLOR", stripe)]
    body = "".join(f'\n        <option name="{k}" value="{v}" />' for k, v in opts if v is not None)
    return f'    <option name="{name}">\n      <value>{body}\n      </value>\n    </option>'


def icls(name, t):
    u, s = t["ui"], t["syntax"]
    bg = u["editor"]
    text, ident = s["punct"], s["ident"]
    green, red, yellow = u["success"], u["error"], u["warning"]
    strong = t["keywordFont"] or None
    search_bg = mix(u["accent"], bg, 0.70)
    caret_ident = mix(u["accent"], bg, 0.85)
    write_ident = mix(s["annotation"], bg, 0.78)

    colors = {
        "CARET_COLOR": t["caret"], "CARET_ROW_COLOR": u.get("caretRow") or mix(bg, "FFFFFF", 0.035),
        "CONSOLE_BACKGROUND_KEY": bg, "GUTTER_BACKGROUND": u["gutter"],
        "LINE_NUMBERS_COLOR": u["lineNumber"],
        "LINE_NUMBER_ON_CARET_ROW_COLOR": u.get("lineNumberActive") or u["text"],
        "INDENT_GUIDE": u["border"], "SELECTED_INDENT_GUIDE": u["thumbHover"], "VISUAL_INDENT_GUIDE": u["border"],
        # La selección de listas (#1C1A1C) es muy sutil para texto; en el editor va teñida de acento.
        "SELECTION_BACKGROUND": u.get("editorSelection") or mix(u["accent"], bg, 0.78), "SELECTION_FOREGROUND": "",
        "TEARLINE_COLOR": u["border"], "SELECTED_TEARLINE_COLOR": u["muted"],
        "RIGHT_MARGIN_COLOR": u["border"], "METHOD_SEPARATORS_COLOR": u["border"],
        "WHITESPACES": u["thumb"], "SOFT_WRAP_SIGN_COLOR": u["thumb"],
        "FOLDED_TEXT_BORDER_COLOR": u["border"],
        "ADDED_LINES_COLOR": mix(green, bg, 0.35), "MODIFIED_LINES_COLOR": mix(s["klass"], bg, 0.35),
        "DELETED_LINES_COLOR": mix(red, bg, 0.35), "WHITESPACES_MODIFIED_LINES_COLOR": mix(yellow, bg, 0.5),
        "ANNOTATIONS_COLOR": u["muted"], "VCS_ANNOTATIONS_COLOR_1": u["raised"],
        "DOCUMENTATION_COLOR": u["panel"], "LOOKUP_COLOR": u["panel"], "NOTIFICATION_BACKGROUND": u["panel"],
        "INFORMATION_HINT": u["raised"], "QUESTION_HINT": u["raised"], "ERROR_HINT": mix(red, bg, 0.8),
        "FILESTATUS_ADDED": green, "FILESTATUS_MODIFIED": s["klass"], "FILESTATUS_DELETED": u["muted"],
        "FILESTATUS_UNKNOWN": red, "FILESTATUS_IGNORED": u["disabled"],
    }

    a = [
        # Fallbacks de la plataforma: los lenguajes heredan de estos DEFAULT_*.
        attr("TEXT", fg=text, bg=bg),
        attr("DEFAULT_IDENTIFIER", fg=ident),
        attr("DEFAULT_KEYWORD", fg=s["keyword"], font=strong),
        attr("DEFAULT_NUMBER", fg=s["number"]),
        attr("DEFAULT_STRING", fg=s["string"]),
        attr("DEFAULT_VALID_STRING_ESCAPE", fg=s["escape"]),
        attr("DEFAULT_INVALID_STRING_ESCAPE", fg=red, effect=red, effect_type=2),
        attr("DEFAULT_LINE_COMMENT", fg=s["comment"], font=2),
        attr("DEFAULT_BLOCK_COMMENT", fg=s["comment"], font=2),
        attr("DEFAULT_DOC_COMMENT", fg=s["doc"], font=2),
        attr("DEFAULT_DOC_COMMENT_TAG", fg=s["doc"], font=3),
        attr("DEFAULT_DOC_MARKUP", fg=s["doc"]),
        attr("DEFAULT_FUNCTION_DECLARATION", fg=s["function"]),
        attr("DEFAULT_FUNCTION_CALL", fg=s["functionCall"]),
        attr("DEFAULT_INSTANCE_METHOD", fg=s["functionCall"]),
        attr("DEFAULT_STATIC_METHOD", fg=s["functionCall"], font=2),
        attr("DEFAULT_CLASS_NAME", fg=s["klass"], font=strong),
        attr("DEFAULT_CLASS_REFERENCE", fg=s["klass"]),
        attr("DEFAULT_INTERFACE_NAME", fg=s["interface"], font=strong),
        attr("DEFAULT_METADATA", fg=s["annotation"]),
        attr("DEFAULT_PARAMETER", fg=ident),
        attr("DEFAULT_LOCAL_VARIABLE", fg=ident),
        attr("DEFAULT_REASSIGNED_LOCAL_VARIABLE", fg=ident, effect=u["muted"], effect_type=1),
        attr("DEFAULT_INSTANCE_FIELD", fg=s["field"]),
        attr("DEFAULT_STATIC_FIELD", fg=s["field"], font=2),
        attr("DEFAULT_GLOBAL_VARIABLE", fg=s["field"]),
        attr("DEFAULT_CONSTANT", fg=s["constant"], font=2),
        attr("DEFAULT_PREDEFINED_SYMBOL", fg=s["keyword"]),
        attr("DEFAULT_LABEL", fg=s["annotation"]),
        attr("DEFAULT_OPERATION_SIGN", fg=s["operator"]),
        attr("DEFAULT_BRACES", fg=s["brace"]), attr("DEFAULT_BRACKETS", fg=text), attr("DEFAULT_PARENTHS", fg=text),
        attr("DEFAULT_DOT", fg=text), attr("DEFAULT_COMMA", fg=text), attr("DEFAULT_SEMICOLON", fg=text),
        attr("DEFAULT_TAG", fg=s["tag"]),
        attr("DEFAULT_ATTRIBUTE", fg=s["attribute"]),
        attr("DEFAULT_ENTITY", fg=s["number"]),
        attr("DEFAULT_TEMPLATE_LANGUAGE_COLOR", fg=text, bg=u["panel"]),
        # Java: Darcula define algunas de estas explícitamente, así que se pisan aquí.
        attr("ANNOTATION_NAME_ATTRIBUTES", fg=s["annotation"]),
        attr("ANNOTATION_ATTRIBUTE_NAME_ATTRIBUTES", fg=s["attribute"]),
        attr("INSTANCE_FIELD_ATTRIBUTES", fg=s["field"]),
        attr("INSTANCE_FINAL_FIELD_ATTRIBUTES", fg=s["field"]),
        attr("STATIC_FIELD_ATTRIBUTES", fg=s["field"], font=2),
        attr("STATIC_FINAL_FIELD_ATTRIBUTES", fg=s["constant"], font=2),
        attr("JAVA_KEYWORD", fg=s["keyword"], font=strong),
        attr("JAVA_NUMBER", fg=s["number"]),
        attr("JAVA_STRING", fg=s["string"]),
        attr("JAVA_VALID_STRING_ESCAPE", fg=s["escape"]),
        attr("JAVA_LINE_COMMENT", fg=s["comment"], font=2),
        attr("JAVA_BLOCK_COMMENT", fg=s["comment"], font=2),
        attr("JAVA_DOC_COMMENT", fg=s["doc"], font=2),
        attr("JAVA_OPERATION_SIGN", fg=s["operator"]),
        attr("CLASS_NAME_ATTRIBUTES", fg=s["klass"], font=strong),
        attr("INTERFACE_NAME_ATTRIBUTES", fg=s["interface"], font=strong),
        attr("METHOD_DECLARATION_ATTRIBUTES", fg=s["function"]),
        attr("CONSTRUCTOR_DECLARATION_ATTRIBUTES", fg=s["function"]),
        attr("METHOD_CALL_ATTRIBUTES", fg=s["functionCall"]),
        attr("CONSTRUCTOR_CALL_ATTRIBUTES", fg=s["functionCall"]),
        attr("STATIC_METHOD_ATTRIBUTES", fg=s["functionCall"], font=2),
        attr("LOCAL_VARIABLE_ATTRIBUTES", fg=ident),
        attr("PARAMETER_ATTRIBUTES", fg=ident),
        attr("TYPE_PARAMETER_NAME_ATTRIBUTES", fg=s["interface"]),
        attr("ENUM_NAME_ATTRIBUTES", fg=s["klass"], font=strong),
        attr("ABSTRACT_CLASS_NAME_ATTRIBUTES", fg=s["klass"], font=3),
        attr("IMPLICIT_ANONYMOUS_CLASS_PARAMETER_ATTRIBUTES", fg=s["field"]),
        attr("JAVA_DOC_TAG", fg=s["doc"], font=3),
        # Estado del editor
        attr("IDENTIFIER_UNDER_CARET_ATTRIBUTES", bg=caret_ident, stripe=s["function"]),
        attr("WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES", bg=write_ident, stripe=s["annotation"]),
        attr("SEARCH_RESULT_ATTRIBUTES", bg=search_bg, stripe=u["accent"]),
        attr("WRITE_SEARCH_RESULT_ATTRIBUTES", bg=write_ident, stripe=s["annotation"]),
        attr("TEXT_SEARCH_RESULT_ATTRIBUTES", fg=u["textBright"], bg=search_bg, stripe=u["accent"]),
        attr("MATCHED_BRACE_ATTRIBUTES", fg=u["textBright"], bg=u["selection"], effect=u["accent"], effect_type=1),
        attr("UNMATCHED_BRACE_ATTRIBUTES", bg=mix(red, bg, 0.7)),
        attr("HYPERLINK_ATTRIBUTES", fg=u["accent"], effect=u["accent"], effect_type=1),
        attr("FOLLOWED_HYPERLINK_ATTRIBUTES", fg=u["accent"], effect=u["accent"], effect_type=1),
        attr("CTRL_CLICKABLE", fg=u["accent"], effect=u["accent"], effect_type=1),
        attr("FOLDED_TEXT_ATTRIBUTES", fg=u["muted"], bg=u["raised"]),
        attr("TODO_DEFAULT", fg=bg, bg=s["interface"], font=1),
        attr("ERRORS_ATTRIBUTES", effect=red, effect_type=2, stripe=red),
        attr("WRONG_REFERENCES_ATTRIBUTES", fg=red),
        attr("WARNING_ATTRIBUTES", effect=yellow, effect_type=2, stripe=yellow),
        attr("WARNINGS_ATTRIBUTES", effect=yellow, effect_type=2, stripe=yellow),
        attr("WEAK_WARNING_ATTRIBUTES", effect=u["muted"], effect_type=2),
        attr("INFO_ATTRIBUTES", effect=u["muted"], effect_type=1),
        attr("NOT_USED_ELEMENT_ATTRIBUTES", fg=u["muted"]),
        attr("DEPRECATED_ATTRIBUTES", effect=u["muted"], effect_type=3),
        attr("MARKED_FOR_REMOVAL_ATTRIBUTES", effect=red, effect_type=3),
        attr("BREAKPOINT_ATTRIBUTES", bg=mix(red, bg, 0.8)),
        attr("EXECUTIONPOINT_ATTRIBUTES", bg=mix(s["klass"], bg, 0.75)),
        attr("INLAY_DEFAULT", fg=u["muted"], bg=u["raised"]),
        attr("INLINE_PARAMETER_HINT", fg=u["muted"], bg=u["raised"]),
        attr("INLINE_PARAMETER_HINT_HIGHLIGHTED", fg=u["textBright"], bg=u["selection"]),
        attr("BOOKMARKS_ATTRIBUTES", stripe=u["accent"]),
        attr("BREADCRUMBS_DEFAULT", fg=u["muted"]),
        attr("BREADCRUMBS_HOVERED", fg=u["textBright"], bg=u["hover"]),
        attr("BREADCRUMBS_CURRENT", fg=u["textBright"], bg=u["selection"]),
        attr("BREADCRUMBS_INACTIVE", fg=u["disabled"]),
        # Diff y merge
        attr("DIFF_INSERTED", bg=mix(green, bg, 0.82), stripe=green),
        attr("DIFF_DELETED", bg=mix(red, bg, 0.82), stripe=red),
        attr("DIFF_MODIFIED", bg=mix(s["klass"], bg, 0.82), stripe=s["klass"]),
        attr("DIFF_CONFLICT", bg=mix(yellow, bg, 0.82), stripe=yellow),
        # Consola
        attr("CONSOLE_NORMAL_OUTPUT", fg=text),
        attr("CONSOLE_ERROR_OUTPUT", fg=red),
        attr("CONSOLE_SYSTEM_OUTPUT", fg=u["muted"]),
        attr("CONSOLE_USER_INPUT", fg=green, font=2),
        attr("LOG_ERROR_OUTPUT", fg=red),
        attr("LOG_WARNING_OUTPUT", fg=yellow),
        attr("LOG_INFO_OUTPUT", fg=text),
        attr("LOG_DEBUG_OUTPUT", fg=u["muted"]),
    ]
    ansi = {"BLACK": u["raised"], "RED": red, "GREEN": green, "YELLOW": yellow, "BLUE": s["klass"],
            "MAGENTA": s["keyword"], "CYAN": s["function"], "GRAY": u["muted"],
            "DARKGRAY": u["disabled"], "WHITE": u["textBright"]}
    for color, value in ansi.items():
        a.append(attr(f"CONSOLE_{color}_OUTPUT", fg=value))
    for color in ("RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN"):
        a.append(attr(f"CONSOLE_{color}_BRIGHT_OUTPUT", fg=mix(ansi[color], "FFFFFF", 0.2)))

    color_lines = "\n".join(f'    <option name="{k}" value="{v}" />' for k, v in colors.items())
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<scheme name="{name}" version="142" parent_scheme="{"Darcula" if t.get("dark", True) else "Default"}">
  <metaInfo>
    <property name="created">{name} color scheme</property>
    <property name="ide">IntelliJ IDEA</property>
    <property name="originalScheme">{name}</property>
  </metaInfo>
  <option name="LINE_SPACING" value="1.0" />
  <option name="EDITOR_FONT_SIZE" value="13" />
  <option name="EDITOR_FONT_NAME" value="JetBrains Mono" />
  <colors>
{color_lines}
  </colors>
  <attributes>
{chr(10).join(a)}
  </attributes>
</scheme>
"""


(OUT / "kuk").mkdir(exist_ok=True)
for icon, fill in (("folder.svg", FOLDER_FILL[True]), ("folder_dark.svg", FOLDER_FILL[True]),
                   ("folder-light.svg", FOLDER_FILL[False])):
    (OUT / "kuk" / icon).write_text(folder_svg(fill), encoding="utf-8", newline="")
for name, t in THEMES.items():
    base = name.replace(" ", "-")
    (OUT / f"{base}.theme.json").write_text(
        json.dumps(theme_json(name, t, f"{base}.xml"), indent=2) + "\n", encoding="utf-8", newline="\n")
    (OUT / f"{base}.xml").write_text(icls(name, t), encoding="utf-8", newline="\n")
    print("ok", base)
