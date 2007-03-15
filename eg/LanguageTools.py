# -*- coding: UTF-8 -*-
# This file is part of EventGhost.
# Copyright (C) 2005 Lars-Peter Voss <lpv@eventghost.org>
# 
# EventGhost is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# EventGhost is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with EventGhost; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#
# $LastChangedDate$
# $LastChangedRevision$
# $LastChangedBy$

import eg
import types
import new

from Utils import SetClass


languageNames = {
    "aa_AA": "Afar",
    "ab_AB": "Abkhazian",
    "af_AF": "Afrikaans",
    "am_AM": "Amharic",
    "ar_AR": "Arabic",
    "as_AS": "Assamese",
    "ay_AY": "Aymara",
    "az_AZ": "Azerbaijani",
    "ba_BA": "Bashkir",
    "be_BE": "Byelorussian",
    "bg_BG": "Bulgarian",
    "bh_BH": "Bihari",
    "bi_BI": "Bislama",
    "bn_BN": "Bengali",
    "bo_BO": "Tibetan",
    "br_BR": "Breton",
    "ca_CA": "Catalan",
    "co_CO": "Corsican",
    "cs_CS": "Czech",
    "cy_CY": "Welsh",
    "da_DA": "Danish",
    "de_DE": "German",
    "dz_DZ": "Bhutani",
    "el_EL": "Greek",
    "en_EN": "English (UK)",
    "en_US": "English (American)",
    "eo_EO": "Esperanto",
    "es_ES": "Spanish",
    "et_ET": "Estonian",
    "eu_EU": "Basque",
    "fa_FA": "Persian",
    "fi_FI": "Finnish",
    "fj_FJ": "Fiji",
    "fo_FO": "Faeroese",
    "fr_FR": "French",
    "fy_FY": "Frisian",
    "ga_GA": "Irish",
    "gd_GD": "Gaelic",
    "gl_GL": "Galician",
    "gn_GN": "Guarani",
    "gu_GU": "Gujarati",
    "ha_HA": "Hausa",
    "hi_HI": "Hindi",
    "hr_HR": "Croatian",
    "hu_HU": "Hungarian",
    "hy_HY": "Armenian",
    "ia_IA": "Interlingua",
    "ie_IE": "Interlingue",
    "ik_IK": "Inupiak",
    "in_IN": "Indonesian",
    "is_IS": "Icelandic",
    "it_IT": "Italian",
    "iw_IW": "Hebrew",
    "ja_JA": "Japanese",
    "ji_JI": "Yiddish",
    "jw_JW": "Javanese",
    "ka_KA": "Georgian",
    "kk_KK": "Kazakh",
    "kl_KL": "Greenlandic",
    "km_KM": "Cambodian",
    "kn_KN": "Kannada",
    "ko_KO": "Korean",
    "ks_KS": "Kashmiri",
    "ku_KU": "Kurdish",
    "ky_KY": "Kirghiz",
    "la_LA": "Latin",
    "ln_LN": "Lingala",
    "lo_LO": "Laothian",
    "lt_LT": "Lithuanian",
    "lv_LV": "Latvian/Lettish",
    "mg_MG": "Malagasy",
    "mi_MI": "Maori",
    "mk_MK": "Macedonian",
    "ml_ML": "Malayalam",
    "mn_MN": "Mongolian",
    "mo_MO": "Moldavian",
    "mr_MR": "Marathi",
    "ms_MS": "Malay",
    "mt_MT": "Maltese",
    "my_MY": "Burmese",
    "na_NA": "Nauru",
    "ne_NE": "Nepali",
    "nl_NL": "Dutch",
    "no_NO": "Norwegian",
    "oc_OC": "Occitan",
    "om_OM": "Oromo/Afan",
    "or_OR": "Oriya",
    "pa_PA": "Punjabi",
    "pl_PL": "Polish",
    "ps_PS": "Pashto/Pushto",
    "pt_PT": "Portuguese",
    "qu_QU": "Quechua",
    "rm_RM": "Rhaeto-Romance",
    "rn_RN": "Kirundi",
    "ro_RO": "Romanian",
    "ru_RU": "Russian",
    "rw_RW": "Kinyarwanda",
    "sa_SA": "Sanskrit",
    "sd_SD": "Sindhi",
    "sg_SG": "Sangro",
    "sh_SH": "Serbo-Croatian",
    "si_SI": "Singhalese",
    "sk_SK": "Slovak",
    "sl_SL": "Slovenian",
    "sm_SM": "Samoan",
    "sn_SN": "Shona",
    "so_SO": "Somali",
    "sq_SQ": "Albanian",
    "sr_SR": "Serbian",
    "ss_SS": "Siswati",
    "st_ST": "Sesotho",
    "su_SU": "Sudanese",
    "sv_SV": "Swedish",
    "sw_SW": "Swahili",
    "ta_TA": "Tamil",
    "te_TE": "Tegulu",
    "tg_TG": "Tajik",
    "th_TH": "Thai",
    "ti_TI": "Tigrinya",
    "tk_TK": "Turkmen",
    "tl_TL": "Tagalog",
    "tn_TN": "Setswana",
    "to_TO": "Tonga",
    "tr_TR": "Turkish",
    "ts_TS": "Tsonga",
    "tt_TT": "Tatar",
    "tw_TW": "Twi",
    "uk_UK": "Ukrainian",
    "ur_UR": "Urdu",
    "uz_UZ": "Uzbek",
    "vi_VI": "Vietnamese",
    "vo_VO": "Volapuk",
    "wo_WO": "Wolof",
    "xh_XH": "Xhosa",
    "yo_YO": "Yoruba",
    "zh_ZH": "Chinese",
    "zu_ZU": "Zulu",
}

    
class EmptyOriginal:
    pass

@eg.LogIt
def LoadStrings(language):   
    #if language == "en_EN":
    #    return
    class tmp:
        pass
    tmp = tmp()
    class MetaClass(type):
        def __new__(metacls, name, bases, dict):
            del dict["__module__"]
            class EmptyTextBunch:
                pass
            cls = new.instance(EmptyTextBunch, dict)
            return cls
    try:
        execfile(
            "Languages\\" + language + ".py", 
            {"__metaclass__": MetaClass}, 
            tmp.__dict__
        )
    except IOError:
        pass
    return tmp



def GetTranslation(cls):
    module = cls.__module__.split(".")[-1]
    trans = getattr(eg.text, module, None)
    if trans is None:
        class trans:
            pass
        trans = trans()
    SetClass(trans, cls)
    setattr(eg.text, module, trans)
    return trans
    
