from pptx.util import Pt, Cm
from pptx.enum.dml import MSO_THEME_COLOR

ENGINEERS = ['Andy Oxford', 'Chris Kelly', 'Luke Phillips', 'Matthew Harbord', 'Neil Griffin']

# Theme Colors
class ThemeColors:
    PINK = MSO_THEME_COLOR.ACCENT_5
    GREEN = MSO_THEME_COLOR.ACCENT_4
    BLUE = MSO_THEME_COLOR.ACCENT_3
    PURPLE = MSO_THEME_COLOR.ACCENT_6
    ORANGE = MSO_THEME_COLOR.ACCENT_2
    TEAL = MSO_THEME_COLOR.ACCENT_1
    BLACK = MSO_THEME_COLOR.TEXT_1
    WHITE = MSO_THEME_COLOR.BACKGROUND_1

STATUS_COLOUR = {
    'Open': ThemeColors.PINK,
    'On Hold': ThemeColors.ORANGE,
    'New': ThemeColors.PURPLE,
    'Blocked': ThemeColors.ORANGE,
}

# File Locations
FILE_LOCATIONS = {
    'project_csv': './raw/PROJECT.csv',
    'document_csv': './raw/DOC.csv',
    'contact_csv': './raw/CONTACT.csv',
    'concession_csv': './raw/CONCESSION.csv',
    'pptx_template': './template/_template.pptx',
}
    
# Text Representations for Staging
STAGING_TEXT_REPRESENTATION = {
    'Triage': "▰▱▱▱▱",
    'Analysis': "▰▰▱▱▱",
    'Alpha Test': "▰▰▰▱▱",
    'Beta Test': "▰▰▰▰▱",
    'Roll-out': "▰▰▰▰▰",
}

# Text Representations for Priority
PRIORITY_TEXT_REPRESENTATION = {
    'P1': "P1 🔥",
    'P2': "P2 🚨",
    'P3': "P3 ⭐",
    'P4': "P4 🐢",
    'P5': "P5 🐌",
}

# Project Button Constants
PROJECT_BUTTON_CONSTANTS = {
    'rectangle_width': Cm(7.8),
    'rectangle_height': Cm(2.8)
}

FOUR_COL_SLIDE_CONSTANTS = {
    'start_left': Cm(0.65),
    'start_top': Cm(2),
    'horizontal_spacing': Cm(0.2),
    'vertical_spacing': Cm(0.2)
}

# Functions
def get_staging_text(staging):
    return STAGING_TEXT_REPRESENTATION.get(staging, "-----")

def get_priority_text(priority):
    return PRIORITY_TEXT_REPRESENTATION.get(priority, "unknown")