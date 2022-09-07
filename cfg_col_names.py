"""
This module contains columns name constants for the VFM project.
"""

RECEIVED_DATE_COL = "aanleverdatum"
PROCESS_DATE_COL = "productiedag"

PROCESS_CODE_COL = "proces_code"

DELIVERY_WINDOW_COL = "bezorgdagkoppel"
DELIVERY_WINDOW_DAY1 = "bezorgdagkoppel1"
DELIVERY_WINDOW_DAY2 = "bezorgdagkoppel2"

LOC_NAME_COL = "locatienaam"
LOC_CODE_COL = "locatiecode"

LOG_PROD_TYPE_COL = "logistiek_productsoort"
LOG_PROD_TYPE_TRS_COL = "logistiek_productsoort_trs"

IMPORT_COL = "import_indicatie"

LOG_SERVICE_COL = "logistiek_servicekader"
LOG_PROD_CODE_COL = "logistiek_productcode"
LOG_PROD_CODE_TRS_COL = "logistiek_productcode_trs"

LOG_ORDER_LINE_COL = "lor_nummer"
LOR_MUTATION_DT_COL = "lor_wijz_timestamp"

COMM_SERVICE_COL_DESCR = "comm_servicekader_omschrijving"
#TODO: Rename "servicekader" to PROCESS_COL = "proces"
COMM_SERVICE_COL = "servicekader"
LOG_SERVICE_COL = "logistiek_servicekader"

MAIL_FLOW_COL = "poststroom"
MAIL_FLOW_TRS_COL = "poststroom_trs"

SORTING_MACHINE_COL = "sorteermachine_type"
SORTING_MACHINE_TRS_COL = "sorteermachine_type_trs"

ORDER_SEEN_COL = "status_waargenomen"
OTE_SEEN_COL = "ote_waargenomen"
SMALL_ORDER_COL = "kleine_order"

TARGET_COL = "aantal_poststukken"
TARGET_COL_RAW = "aantal_poststukken_raw"

TEMP_DATE_COL = "production_day"
WEEKDAY_COL = "weekday"
DATE_OF_PRED_COL = "date_of_prediction"
T_COL = "t"
T_WEEKS_COL = "t_weeks"
PREDICTION_COL = "predict"
