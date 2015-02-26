# -*- coding: utf-8 -*-


def fix_news_carousel_source(context):
    """Fix source for home carousel."""
    context.runImportStepFromProfile('profile-sac.aerofacil:default', 'portlets')
    context.runImportStepFromProfile('profile-sac.aerofacil:upgrade_to_1001', 'viewlets')
