
class Interface:
    FREE_SIGN = "sevend/free_sign/"
    weixinPrefix = "sevend/weixin/"

    # account-center
    GET_VERIFY_CODE = "sevend/get_verify_code" # 获取图形验证码
    GET_WEB_VERIFY_CODE = "sevend/get_web_verify_code" # 获取图形验证码
    SEND_REGISTER_SMS = "sevend/send_register_sms" # 发送注册短信验证码
    SEND_INVITE_REGISTER_SMS = "sevend/send_invite_register_sms" # 发送邀请注册短信，不校验图形验证码
    RESEND_REGISTER_SMS = "sevend/resend_register_sms" # 重发注册短信验证码
    CHECK_REGISTER_SMS = "sevend/check_register_sms" # 校验注册短信验证码
    REGISTER = "sevend/register" # 设置密码完成注册
    WEB_REGISTER = "sevend/web_register" # 设置密码完成注册
    WEB_SIMPLE_REGISTER = "sevend/web_simple_register" # 设置密码完成注册

    # 验证码登录相关
    ENTRANCE_INFO = "sevend/entrance_info" # 获取手机号码注册相关信息
    CHECK_SMS_CODE = "sevend/check_sms_code" # 校验图形验证码
    SEND_SMS_CODE = "sevend/send_sms_code" # 发送验证码
    LOGIN_WITH_SMSCODE = "sevend/login_with_smscode" # 验证码登录

    # 保宝网渠道注册相关
    SEND_REGISTER_SMS_CONDITON = "sevend/send_register_sms_condition" # 发送短信验证码

    CHECK_SMS_STATUS = "sevend/check_sms_status" # 是否已经发送短信验证码
    # H5商户
    SEND_CHANNEL_SMS = "sevend/send_channel_sms" # 发送短信验证码

    REFRESH_SESSION_KEY = "sevend/refresh_session_key" # 刷新 session_key
    LOGIN = "sevend/login" # 登录
    MODIFY_PWD = "sevend/modify_pwd" # 修改登录密码
    RESET_PWD = "sevend/reset_pwd" # 重置登录密码
    LOGOUT = "sevend/logout" # 退出登录
    GET_USER_INFO = "sevend/get_user_info" # 拉取用户信息
    GET_QINIU_UPTOKEN = "sevend/get_qiniu_uptoken" # 获取七牛上传token
    UPDATE_GETUI_ID = "sevend/update_getui_id" # 更新用户个推ID

    START_UP = "sevend/start_up" # app启动上报数据
    GET_INVITE_INFO = "sevend/get_app_invite_info"
    GET_INVITE_TIP = "sevend/get_app_invite_tip"
    ENTRANCE = "sevend/entrance" # 检查手机号是否注册
    FROZEN = "sevend/frozen" # 用户冻结
    FROZEN_WITH_STRATEGY = "sevend/frozen_with_strategy" # 用户冻结

    DO_APP_INVITE_INSURED = "sevend/do_app_invite_insured" # 3.7 判断邀请投保人活动是否上线

    # loan-centerx
    SEND_LOAN_SMS = "sevend/send_loan_sms" # 发送借款短信
    GET_LOAN_AGREEMENT = "sevend/get_loan_agreement" # 获取借款协议
    GET_LOAN_AGREEMENT_BY_CHANNEL = "sevend/get_loan_agreement_by_channel" # 获取借款协议
    GET_CHANNEL_PROTOCOL = "sevend/get_channel_protocol" # 获取渠道的借款协议
    LOAN_AUDIT_NOTIFY = "sevend/loan_audit_notify" # 湖北审核回调
    CANCEL_LOAN_ORDER = "sevend/cancel_loan_order"
    ACTIVE_CANCEL_LOAN = "sevend/active_cancel_loan"
    GET_USER_HOME_INFO = "sevend/get_user_home_info"
    GET_HOME_INFO = "sevend/get_home_info"
    GET_ANNUAL_INCOMES_LIST = "sevend/get_annual_incomes_list"
    # payment-center
    SET_TRADE_PASSWORD = "sevend/set_trade_password"
    BIND_BANK_CARD = "sevend/bind_bank_card"
    BIND_BANK_CARD_WITH_CITY = "sevend/bind_bank_card_with_city"
    RESEND_MESSAGE = "sevend/resend_message"
    CONFIRM_PAY = "sevend/confirm_pay"
    MODIFY_TRADE_PASSWORD = "sevend/modify_trade_password"
    QUERY_BANK_CARD_LIST = "sevend/query_bank_card_list"
    QUERY_SECURITY_BANK_CARD = "sevend/query_security_bank_card"
    QUERY_BANK_CODE_NAME_MAPPING = "sevend/query_bank_code_name_mapping"
    QUERY_BANK_CODE_NAME_MAPPING_NEW_V2 = "sevend/query_bank_code_name_mapping_v2"
    VALID_TRADE_PASSWORD = "sevend/valid_trae_password"
    QUICK19_PAY_NOTIFY = "sevend/quick19_pay_notify"
    WITHDRAW19_NOTIFY = "sevend/withdraw19_notify"
    WITHHOLD19_NOTIFY = "sevend/withhold19_notify"
    GET_SMS_FOR_FORGET_TRADEPASSWORD_CODE = "sevend/get_sms_for_forget_tradepassword_code"
    FORGET_TRADEPASSWORD_INFO_CONFIRM = "sevend/forget_tradepassword_info_confirm"
    RESEND_SMS_FOR_TRADEPASSWORD_CODE = "sevend/resend_sms_for_tradepassword_code"
    CHECK_CUSTOMER_HAS_TRADE_PASSWORD = "sevend/check_customer_has_trade_password"
    QUICK19_REAL_NAME_AUTH = "sevend/quick19_real_name_auth"
    WITHDRAW_JYT_NOTIFY = "sevend/jyt_withdraw_notify"
    WITHHOLD_JYT_NOTIFY = "sevend/jyt_withhold_notify"

    # repay-center

    GET_REPAY_LIST = "sevend/get_repay_list" # 还款记录4.0
    GET_REPAY_DETAIL = "sevend/get_repay_detail" # 还款订单详情4.0

    # push-center
    GET_MSG_LIST = "sevend/get_msg_list" # 拉取消息列表
    GET_MSG_DETAIL = "sevend/get_msg_detail" # 拉取消息详情
    REPORT_MSG_ARRIVE = "sevend/report_msg_arrive" # 消息到达上报
    GET_RED_DOT = "sevend/get_red_dot" # 拉取小红点

    # credit
    PARTNER_QUOTA_MODIFY_CALL_BACK = "sevend/partner_quota_modify_call_back"

    # free sign credit 免签信审
    FREE_SIGN_AUTH_REQUEST = FREE_SIGN + "free_sign_auth_request"
    FREE_SIGN_GET_USER_ID = FREE_SIGN + "free_sign_get_user_id"

    # 用户反馈
    FEEDBACK = "sevend/feedback"

    # data-center
    REPORT_APP_CUSTOMER_DATA = "sevend/get_customer_info"
    GET_LAST_REPORT_DATA_ID = "sevend/get_customer_id"
    GET_LATEST_VERSION = "sevend/get_latest_version"

    # APP
    GET_PUB_KEY = "sevend/get_pub_key"
    GET_HOME_BANNER = "sevend/get_home_banner"

    # bag-center
    GET_SUMMARY = "sevend/get_summary"
    GET_MONTH_INSURANCE_ORDERS = "sevend/get_month_insurance_orders"
    GET_TODO_SCHEDULES = "sevend/get_todo_schedules"
    CANCEL_TODO_SCHEDULE = "sevend/cancel_todo_schedule"
    MODIFY_TODO_SCHEDULE = "sevend/modify_todo_schedule"
    ADD_INSURANCE_ORDER = "sevend/add_insurance_order"
    GET_INSURANCE_ORDERS = "sevend/get_insurance_orders"
    GET_INSURANCE_ORDER_DETAIL = "sevend/get_insurance_order_detail"
    DEL_INSURANCE_ORDER = "sevend/del_insurance_order"
    ADD_POSSIBLE_CUSTOMER = "sevend/add_possible_customer"
    GET_POSSIBLE_CUSTOMERS = "sevend/get_possible_customers"
    GET_POSSIBLE_CUSTOMER_DETAIL = "sevend/get_possible_customer_detail"
    DEL_POSSIBLE_CUSTOMER = "sevend/del_possible_customer"

    # cfca
    GET_CFCA_STATE = "sevend/get_cfca_state"
    EXTSIGN_AUTO_NOTIFY = "sevend/extsign_auto_notify"

    # dial-test
    DIAL_TEST = "sevend/dial_test"

    # inner
    INNER_QUERY_KFT_BALANCE = "sevend/query_kft_balance"
    INNER_QUERY_CHANNEL_BALANCE = "sevend/query_channel_balance"
    INNER_QUERY_FINANCE_PLAN_INFO = "sevend/query_finance_plan_info"
    INNER_CHANGE_FINANCE_PLAN = "sevend/change_finance_plan"
    INNER_QUERY_CASH_FINANCE_PLAN_INFO = "sevend/query_cash_finance_plan_info"
    INNER_CHANGE_CASH_FINANCE_PLAN = "sevend/change_cash_finance_plan"
    # 资金分期卡配置
    QUERY_FQK_FINANCE_PRIORITY = "sevend/query_fqk_finance_priority"
    CHANGE_FQK_FINANCE_PRIORITY = "sevend/change_fqk_finance_priority"
    QUERY_FQK_FINANCE_PLAN_INFO = "sevend/query_fqk_finance_plan_info"
    CHANGE_FQK_FINANCE_PLAN = "sevend/change_fqk_finance_plan"

    # policy
    CHECK_POLICYHOLDERS_APPLY_PERSONAL_INFO = "sevend/check_policyholders_apply_personal_info"
    CHECK_POLICYHOLDERS_APPLY_INSURANCE_INFO = "sevend/check_policyholders_apply_insurance_info"
    POLICYHOLDERS_APPLY = "sevend/policyholders_apply"
    GET_WITHDRAW_SUMMARY = "sevend/get_withdraw_summary"
    GET_POLICYHOLDERS_APPLY_LIST = "sevend/get_policyholders_apply_list"
    GET_POLICYHOLDERS_APPLY_DETAIL = "sevend/get_policyholders_apply_detail"
    GET_POLICYHOLDERS_WITHDRAW_LIST = "sevend/get_policyholders_withdraw_list"
    GET_POLICYHOLDERS_WITHDRAW_DETAIL = "sevend/get_policyholders_withdraw_detail"
    GET_REPAY_PLAN_LIST = "sevend/get_repay_plan_list"
    GET_REPAY_PLAN_LIST_LOAN_POLICY = "sevend/get_repay_plan_list_loan_policy"
    CANCEL_POLICYHOLDERS_APPLY = "sevend/cancel_policyholders_apply"
    POLICYHOLDERS_AUTO_AUDIT_CALLBACK = "sevend/policy_auto_audit_callback"
    CAN_POLICYHOLDERS_APPLY = "sevend/can_policyholders_apply"
    LARGE_AMOUNT_LOAN_CARD_LIST = "sevend/large_amount_loan_card_list"
    LARGE_AMOUNT_LOAN = "sevend/large_amount_loan"
    LARGE_AMOUNT_LOAN_LIST = "sevend/large_amount_loan_list"
    GET_POLICY_COMPANY = "sevend/get_policy_company"
    POLICYHOLDERS_QIYE_AUTH = "sevend/policyholders_qiye_auth"
    POLICYHOLDERS_QIYE_UNBIND = "sevend/policyholders_qiye_unbind"
    CHECK_QIYE_ORDER_NO = "sevend/check_qiye_order_no"
    QIYE_POLICYHOLDERS_APPLY = "sevend/qiye_policyholders_apply"
    QIYE_SALER_PAY_INTEREST_SMS = "sevend/qiye_saler_pay_interest_sms"
    QIYE_SALER_PAY_INTEREST_CONFIRM = "sevend/qiye_saler_pay_interest_confirm"
    GET_CAR_LICENSE_NO_BY_GPS = "sevend/get_car_license_no_by_gps"
    GET_UPLOAD_PHOTO_TYPE = "sevend/get_upload_photo_type"
    POLICY_INSTALMENTS_APPLY = "sevend/policy_instalments_apply"
    POLICY_INSTALMENTS_APPLY_LOAN = "sevend/policy_instalments_apply_loan"
    QIYE_POLICY_INSTALMENTS_APPLY = "sevend/qiye_policy_instalments_apply"

    # 首借活动
    ACTIVITY_NEW_USER_GET_BASE_INFO = "sevend_act/activity_new_user_get_base_info"

    # 会员日活动
    GET_VIP_DAY_INFO = "sevend_act/vip_day_info" # 查询抽奖次数和活动时间
    VIP_DAY_DRAW = "sevend_act/vip_day_draw" # 抽奖
    VIP_DAY_PRIZE_LIST = "sevend_act/vip_day_prize_list" # 已中奖品
    VIP_DAY_PRIZES = "sevend_act/vip_day_prizes" # 已中奖品
    VIP_DAY_QUERY_LAST_LOAN = "sevend_act/vip_day_query_last_loan" # 最近借款人

    # 五月夺宝活动
    MAY_DRAW_BASE_INFO = "sevend_act/may_draw_base_info"
    MAY_DRAW_CURRENT_INFO_LIST = "sevend_act/may_draw_current_info_list"
    MAY_DRAW_CURRENT_INFO = "sevend_act/may_draw_current_info"
    MAY_DRAW = "sevend_act/may_draw"
    MAY_DRAW_RECORDS = "sevend_act/may_draw_records"
    MAY_DRAW_RECORD_DETAIL = "sevend_act/may_draw_record_detail"
    MAY_DRAW_JOIN_RECORDS = "sevend_act/may_draw_join_records"

    # 微信增粉活动
    WX_FANS_GET_BASE_INFO = "sevend_act/wx_fans_get_base_info"
    WX_FANS_GET_ALL_PRIZE = "sevend_act/wx_fans_get_all_prize"
    WX_FANS_QUERY_LATEST_TOP_WINNER = "sevend_act/wx_fans_query_latest_top_winner"
    WX_FANS_DRAW = "sevend_act/wx_fans_draw"
    WX_WX_GET_JS_SDK_SIGN = "sevend_act/wx_get_js_sdk_sign"
    WX_FANS_V2_SEND_FREE_TICKET = "sevend_act/wx_fans_v2_send_free_ticket"
    WX_GET_ACT_MOBILE_LIST = "sevend_act/wx_get_act_mobile_list"

    # 现金活动
    ACTIVITY_CASH_GET_BASE_INFO = "sevend_act/activity_cash_get_base_info"
    ACTIVITY_CASH_DRAW = "sevend_act/activity_cash_draw"
    ACTIVITY_CASH_QUERY_MY_PRIZE = "sevend_act/activity_cash_query_my_prize"
    # 增值包折扣活动
    ACTIVITY_EXTRA_DISCOUNT = "sevend_act/activity_extra_discount"
    # 活动列表
    QUERY_ACTIVITY_LIST = "sevend_act/query_activity_list"

    # SummerDay活动
    SUMMER_DAY_QUERY_SUMMER_DAY_INFO = "sevend_act/summer_day_query_summer_day_info"
    SUMMER_DAY_QUERY_CITY_DETAIL = "sevend_act/summer_day_query_city_detail"
    SUMMER_DAY_OPEN_PRIZE = "sevend_act/summer_day_open_prize"
    SUMMER_DAY_DRAW_PRIZE = "sevend_act/summer_day_draw_prize"
    SUMMER_DAY_LIST_MY_PRIZE = "sevend_act/summer_day_list_my_prize"
    SUMMER_DAY_QUERY_ONE_REACHED_CITY_DETAIL = "sevend_act/summer_day_query_one_reached_city_detail"
    SUMMER_DAY_QUERY_LATEST_WINNER = "sevend_act/summer_day_query_latest_winner"

    # MGM活动
    MGM_RED_PACKET_INFO = "sevend_act/mgm_red_packet_info"
    MGM_DRAW_ONE_RED_PACKET = "sevend_act/mgm_draw_one_red_packet"

    # 信用节活动
    CREDIT_DAY_GET_BASE_INFO = "sevend_act/credit_day_get_base_info"
    CREDIT_DAY_GET_RANK_LIST = "sevend_act/credit_day_get_rank_list"
    QUERY_LATEST_TOP_WINNER = "sevend_act/query_latest_top_winner"
    CREDIT_DAY_GET_QUOTA_DETAILS = "sevend_act/credit_day_get_quota_details"
    CREDIT_DAY_GRAB_QUOTA = "sevend_act/credit_day_grab_quota"

    # MGMV2活动
    MGM_V2_GET_BASE_INFO = "sevend_act/mgm_v2_get_base_info"
    MGM_V2_GET_ALL_INVITE_LEVEL = "sevend_act/mgm_v2_get_all_invite_level"
    MGM_V2_GET_INVITE_LEVEL_DETAIL = "sevend_act/mgm_v2_get_invite_level_detail"

    # MGMV3活动
    MGM_V3_GET_BASE_INFO = "sevend_act/mgm_v3_get_base_info"
    MGM_V3_DRAW_PRIZE = "sevend_act/mgm_v3_draw_prize"

    # 用户群精细运营活动
    DUAL_GIFT_GET_BASE_INFO = "sevend_act/dual_gift_get_base_info"
    DUAL_GIFT_GET_FIRST_RED_PACKET = "sevend_act/dual_gift_get_first_red_packet"
    DUAL_GIFT_GET_SECOND_RED_PACKET = "sevend_act/dual_gift_get_second_red_packet"

    # MGMV3活动
    INSURER_PACKET_SAVE_MOBILE = "sevend_act/insurer_packet_save_mobile"

    # 会员预热活动
    MEMBER_PREHEAT_BASE_INFO = "sevend_act/member_preheat_base_info"
    MEMBER_PREHEAT_ACTIVATE = "sevend_act/member_preheat_activate"

    # 会员预热活动
    LOANOFF_BASE_INFO = "sevend_act/loanoff_base_info"
    LOANOFF_SET_CUSTOMER_TYPE = "sevend_act/loanoff_set_customer_type"

    # 2019四月踏青活动
    OUT_SPRING_INFO = "sevend_act/out_spring_info"
    OUT_SPRING_RECEIVE_AWARD = "sevend_act/receive_award"

    # 2019周年庆活动
    ANNIVERSARY_INFO = "sevend_act/anniversary_info"
    ANNIVERSARY_ADD = "sevend_act/anniversary_add"
    ANNIVERSARY_DRAW = "sevend_act/anniversary_draw"
    ANNIVERSARY_PRIZE_LIST = "sevend_act/anniversary_prize_list"
    ANNIVERSARY_PRIZES = "sevend_act/anniversary_prizes"

    # 2019 7月夺宝活动
    TREASURE_INFO = "sevend_act/treasure_info"
    TREASURE_DRAW = "sevend_act/treasure_draw"
    TREASURE_PRIZE_LIST = "sevend_act/treasure_prize_list"

    # 2019 7 月返现活动
    CASH_BACK_INFO = "sevend_act/cash_back_info"
    CASH_BACK_CHECK = "sevend_act/cash_back_check"
    CASH_BACK_PRIZE_LIST = "sevend_act/cash_back_prize_list"
    CASH_BACK_PRIZES = "sevend_act/cash_back_prizes"

    # free interest ticket
    GET_USER_TICKETS = "sevend/get_user_tickets"
    SEND_INTEREST_TICKET = "sevend/send_interest_ticket"
    SEND_INTEREST_TICKET_LIST = "sevend/send_interest_ticket_list"
    # 预审
    POLICYHOLDERS_PRE_APPLY_AUTO_AUDIT_CALLBACK = "sevend/policy_pre_apply_auto_audit_callback"
    GET_PRE_POLICYHOLDERS_APPLYS = "sevend/get_pre_policyholders_applys"
    PRE_POLICYHOLDERS_APPLY = "sevend/pre_policyholders_apply"
    DEL_PRE_POLICYHOLDERS_APPLY = "sevend/del_pre_policyholders_apply"

    # 7贷4.0接口
    # 通知栏和首页轮播banner接口
    GET_BANNER = "sevend/get_banner"
    # 弹屏广告banner
    GET_TOAST_AD = "sevend/get_toast_ad" # 获取弹屏广告
    # 借款
    GET_LOAN_LIST = "sevend/get_loan_list" # 拉取借款记录
    # 授信
    IDENTIFY_INFO_SUBMIT = "sevend/identify_info_submit" # 提交个人信息
    WORK_INFO_SUBMIT = "sevend/work_info_submit" # 提交工作信息
    EMERGENCY_CONTACTS_INFO_SUBMIT = "sevend/emergency_contacts_info_submit" # 紧急联系人信息提交
    GET_PERSONAL_AUTH_ITEMS = "sevend/get_personal_auth_items" # 拉取信用授权项
    PERSONAL_AUTH_SUBMIT = "sevend/personal_auth_submit" # 认证结果提交
    RESIDENTIAL_INFO_SUBMIT = "sevend/residential_info_submit" # 居住地址信息提交
    JOB_ADDRESS_SUBMIT = "sevend/job_address_submit" # 居住地址信息提交
    GET_ADDRESS_INFO = "sevend/get_address_info" # 获取用户地址信息

    # 工作城市定位
    PARTNER_JOB_AREA_SUBMIT = "sevend/partner_job_area_submit" # 提交工作城市
    AUTH_ITEMS_SUBMIT = "sevend/auth_items_submit" # 信用授权提交

    PARTNER_AUTH_CALL_BACK = "sevend/partner_auth_call_back" # 授权项回调
    # 拉取资料补充的结果
    GET_COMPLETE_INFO_STATUS = "sevend/get_complete_info_status"
    COMPLETE_USER_INFO = "sevend/complete_user_info" # 用户信息补全

    # 代理人认证
    GET_AGENCY = "sevend/get_agency"

    NEW_GET_USER_INFO = "sevend/new_get_user_info"
    BUILD_BANK_CARD_LOAN = "sevend/build_bank_card_loan"
    GET_PARTNER_ALL_SUBMIT_INFO = "sevend/get_partner_all_submit_info"
    GET_PARTNER_CREDIT_STATUS = "sevend/get_partner_credit_status"

    # 商城分期后台相关
    MALL_GET_CUSTOMER_INFO = "sevend_mall/get_customer_info"
    MALL_GET_REPAY_EACH_PERIOD_BATCH = "sevend_mall/get_repay_each_period_batch"
    MALL_QUERY_LOAN_ORDER = "sevend_mall/query_loan_order"
    MALL_UPDATE_ORDER_STATUS = "sevend_mall/update_order_status"
    SEND_PUSH = "sevend_mall/send_push"

    MALL_LOAN_WITHOUT_SMS = "sevend_mall/mall_loan_without_sms"
    MALL_GET_CUSTOMER_QUOTA = "sevend_mall/get_customer_quota"
    GET_UN_REAPAY_PRINCIPAL = "sevend_mall/get_un_reapay_principal"
    MALL_GET_REPAY_PLAN = "sevend_mall/get_repay_plan"

    # 商城分期app相关
    MALL_APP_GET_REPAY_EACH_PERIOD = "/sevend_mall_app/get_repay_each_period"
    MALL_APP_GET_REPAY_PLAN = "/sevend_mall_app/get_repay_plan"
    MALL_APP_SEND_LOAN_SMS = "/sevend_mall_app/send_loan_sms"
    MALL_APP_LOAN_CONFIRM = "/sevend_mall_app/loan_confirm"

    # 4.0反欺诈借款接口
    LOAN_WITH_RC = "sevend/loan_with_rc"

    # 拉取借款
    GET_LOAN_INFO = "sevend/get_loan_info"

    # 查询还款计划
    QUERY_REPAY_PLAN = "sevend/query_repay_plan"
    # 查询借款详情（包括还款计划）
    GET_LOAN_REPAY_DETAIL = "sevend/get_loan_repay_detail"
    # 查询借款结果
    GET_LOAN_RESULT = "sevend/get_loan_result"
    # 使用外部页面借款 成功回调
    LOAN_WEB_CALLBACK = "sevend/loan_web_callback"

    # 获取用户当前银行卡
    GET_CURRENT_BANK_CARD = "sevend/get_current_bank_card"
    # 查询用户还款计划
    QUERY_USER_REPAY_PLAN_LIST = "sevend/query_user_repay_plan_list"
    # 查询本期/某期应还
    QUERY_USER_REPAY_PLAN_BY_TIME = "sevend/query_user_repay_plan_by_time"
    # 查询待还款借款订单
    GET_WAIT_REPAY_LIST = "sevend/get_wait_repay_list"
    # 还款试算
    REPAY_TRY_CALC = "sevend/repay_try_calc"
    # 安全卡还款发验证码
    SEND_REPAY_BINDING_CARD_SMS = "sevend/send_repay_binding_card_sms"
    # mgm活动banner借还款banner
    GET_LOAN_AFTER_BANNER = "sevend/get_loan_after_banner"

    GET_MORE_REPAY_TYPE = "sevend/get_more_repay_type"
    WEIXIN_REPAY = "sevend/weixin_repay"
    WEIXIN_REPAY_CONFIRM = "sevend/weixin_repay_confirm"

    # banner管理相关接口
    QUERY_BANNER_LIST = "sevend/query_banner_list"
    QUERY_ACTIVITY_BANNER_KEYS = "sevend/query_activity_banner_keys"
    QUERY_BANNER_DETAIL = "sevend/query_banner_detail"
    CHANGE_BANNER = "sevend/change_banner"
    ADD_BANNER = "sevend/add_banner"
    DELETE_BANNER = "sevend/delete_banner"

    # 查询支持的借款种类
    GET_SUPPORT_LOAN_TYPE = "sevend/get_support_loan_type"
    # 发送 重发 借款短信
    SEND_INSTALMENT_LOAN_SMS = "sevend/send_instalment_loan_sms"
    # 分期借款应还明细试算
    CALC_INSTALMENT_LOAN_REPAY_PLAN = "sevend/calc_instalment_loan_repay_plan"
    # 分期借款确认
    CONFIRM_INSTALMENT_LOAN = "sevend/confirm_instalment_loan"
    # 七鱼客服
    GET_INFO_FOR_QIYU = "sevend/get_info_for_qiyu"

    # 会员中心相关接口
    QUERY_CUSTOMER_MEMBER_INFO = "sevend/query_customer_member_info"
    # 查询会员等级，成长值
    QUERY_CUSTOMER_MEMBER_GRADE = "sevend/query_customer_member_grade"

    # APP欢迎页(闪屏)和浮标banner
    GET_START_UP_BANNER = "sevend/get_start_up_banner"
    # 首页浮标
    GET_HOME_PAGE_BUOY = "sevend/get_home_page_buoy"
    # 判断当前版本是否是审核版本
    GET_CURRENT_INFO = "sevend/get_current_info"
    # 判断当前版本是否是包装APP版本
    GET_CURRENT_VERSION = "sevend/get_current_version"

    # 会员积分模块
    MEMBER_POINTS_GET_BASE_INFO = "sevend/member_points_get_base_info"
    MEMBER_POINTS_GET_EXCHANGEABLE_PRODUCTS = "sevend/member_points_get_exchangeable_products"
    MEMBER_POINTS_QUERY_POINTS_WATERS = "sevend/member_points_query_points_waters"
    MEMBER_POINTS_EXCHANGE_POINTS = "sevend/member_points_exchange_points"
    MEMBER_POINTS_GET_EXCHANGEABLE_PRODUCT_DETAIL = "sevend/member_points_get_exchangeable_product_detail"

    # 签到
    MEMBER_CHECH = "sevend/member_check"

    # 商城分期
    MALL_INSTALMENT_GET_REPAY_EACH_PERIOD_BATCH = "sevend_mall/get_instalment_repay_each_period_batch"
    MALL_INSTALMENT_GET_REPAY_PLAN = "sevend_mall/get_instalment_repay_plan"
    MALL_INSTALMENT_LOAN_WITHOUT_SMS = "sevend_mall/mall_instalment_loan_without_sms"

    # 提额
    QUERY_IMPROVE_QUOTA_INFO = "sevend/query_improve_quota_info"
    APPLY_UPGRADE_QUOTA = "sevend/apply_upgrade_quota"
    GET_PERSONAL_AUTH_ITEMS_FOR_IMPROVE_QUOTA = "sevend/get_personal_auth_items_for_improve_quota"

    # 通用banner
    GET_CURRENCY_BANNER = "sevend/get_currency_banner"

    # 获取芝麻信用授权URL
    GET_ZMXY_AUTH_URL = "sevend/get_zmxy_auth_url"
    # 芝麻信用授权回调
    ZMXY_AUTH_CALL_BACK = "sevend/zmxy_auth_call_back"

    # 微信
    # 微信-接收消息
    WX_RECEIVE_WEIXIN_MSG = "sevend/receive_weixin_msg"
    # 微信-回调
    WX_REDIRECT = "sevend/wx_redirect"

    WX_MALL_REDIRECT = "sevend/wx_mall_redirect"
    # 微信-JS签名
    WX_GET_JS_SDK_SIGN = "sevend/wx_get_js_sdk_sign"
    # 微信-商城JS签名
    WX_MALL_GET_JS_SDK_SIGN = "sevend/wx_mall_get_js_sdk_sign"
    # open_id是否绑定
    WEXIN_HAS_BIND = "sevend/weixin_has_bind"
    # 公众号绑定
    WEIXIN_BIND = "sevend/weixin_bind"

    # 认证中心
    QUERY_AUTHENTICATION_ITEMS = "sevend/query_authentication_items"
    QUERY_AUTHENTICATION_ITEM_DETAIL = "sevend/query_authentication_item_detail"
    QUERY_AUTHENTICATION_NOTIFY = "sevend/authentication_notify"
    SEND_HAIER_SIGN_PAY_SMS = "sevend/send_haier_sign_pay_sms"
    CONFIRM_HAIER_SIGN_PAY_SMS = "sevend/confirm_haier_sign_pay_sms"
    SEND_SZS_SIGN_PAY_SMS = "sevend/send_szs_sign_pay_sms"
    CONFIRM_SZS_SIGN_PAY_SMS = "sevend/confirm_szs_sign_pay_sms"
    AUTHENTICATION_QUERY_PASSWORD = "sevend/authentication_query_password"
    AUTHENTICATION_RESET_PASSWORD = "sevend/authentication_reset_password"
    AUTHENTICATION_SUBMIT_PASSWORD = "sevend/authentication_submit_password"

    # 协议支付
    QUERY_SIGN_PAY_ITEMS = "sevend/query_sign_pay_items"
    QUERY_SIGN_PAY_ITEM_DETAIL = "sevend/query_sign_pay_item_detail"
    SEND_SIGN_PAY_SMS = "sevend/send_sign_pay_sms"
    CONFIRM_SIGN_PAY_SMS = "sevend/confirm_sign_pay_sms"
    QUERY_NEED_SIGN_PAY = "sevend/query_need_sign_pay"

    SET_CUSTOMER_EMAIL = "sevend/set_customer_email"

    GET_OVERDUE_DETAIL_TIPS = "sevend/get_overdue_detail_tips" # 获取逾期文案

    SET_CUSTOMER_JOB_TYPE = "sevend/set_customer_job_type"
    QUERY_CREDIT_CARD_INFO = "sevend/query_credit_card_info"
    QUERY_CUSTOMER_JOB_TYPE_INFO = "sevend/query_customer_job_type_info"

    # v4.6.0延期需求
    POSTPONE_ORDER_DETAIL = "/sevend/postpone_order_detail" # 延期订单详情
    SEND_POSTPONE_ORDER = "/sevend/send_postpone_order" # 支付手续费并账单延期
    REPAY_POSTPONE_ORDER_DETAIL = "/sevend/repay_postpone_order_detail" # 应还总金额明细
    POSTPONE_WITH_SMS = "/sevend/postpone_with_sms" # 验证码确认账单延期
    POSTPONE_ORDER_RESULT_DETAIL = "/sevend/postpone_order_result_detail" # 账单延期订单借款结果详情
    GET_POSTPONE_LOAN_AGREEMENT = "/sevend/get_postpone_loan_agreement" # 获取账单延期借款协议
    GET_POSTPONE_ORDER_REPAY_PLAN = "/sevend/get_postpone_order_repay_plan" # 延期账单新借款金额明细
    BUILD_EXTENSION_REPAY_PLAN = "/sevend/build_extension_repay_plan"# 获取预期金额应还金额，延期手续费详情

    # 反欺诈
    ANTI_FRAUD_RESULT = "/sevend/anti_fraud_result"

    USERBEHAVIOR_AUTH = "/sevend/behavior/auth"
    USERBEHAVIOR_LOAN_BEHAVIRO_RECORD = "/sevend/behavior/loan_behavior_record"
    USERBEHAVIOR_ALL_CHANNEL = "/sevend/behavior/all_channel"

    # 新授信流程
    GET_CREDIT_INFO = "sevend/get_credit_info"
    QUERY_JOB_INFO = "sevend/query_job_info"
    JOB_INFO_SUBMIT = "sevend/job_info_submit"
    QUERY_POLICY_INFO = "sevend/query_policy_info"
    POLICY_INFO_SUBMIT = "sevend/policy_info_submit"
    GET_INSURANCE_COMPANY_LIST = "sevend/get_insurance_company_list"
    GET_INVITE_AUTH_ITEMS = "sevend/get_invite_auth_items"

    # 麦芒对接接口文档
    # 检验手机号是否已注册
    MAI_MANG_QUERY_USER_INFO = "sevend/mai_mang/query_user_info"
    # 发送绑卡验证码
    MAIMANG_SEND_BIND_CARD_SMS = "sevend/mai_mang/send_bind_card_sms"
    # 确认绑卡
    MAIMANG_CONFIRM_BIND_CARD = "sevend/mai_mang/confirm_bind_card"
    # 申请授信
    MAIMANG_APPLY_AUDIT = "sevend/mai_mang/apply_audit"
    # 查询授信结果
    MAIMANG_QUERY_AUDIT_RESULT = "sevend/mai_mang/query_audit_result"
    # 麦芒发优惠券
    MAI_MANG_SEND_FREE_TICKET = "sevend/mai_mang/send_free_ticket"
    # 麦芒上传通讯录和通话记录
    MAI_MANG_GET_UPLOAD_TOKEN = "sevend/mai_mang/get_upload_token"
    CALL_BACK_FOR_QINIU = "sevend/call_back_for_qiniu"

    MAIMANG_HOME_PAGE = "sevend/mai_mang/home_page"

    # 通过借款接口
    BUILD_REPAY_PLAN = "sevend/build_repay_plan"
    LOAN = "sevend/loan"
    LOAN_CONFIRM = "sevend/loan_confirm"

    CONFIRM_LOAN_AMOUNT = "sevend/confirm_loan_amount"

    CLICK_EXTENSION_BTN = "sevend/click_extension_btn"

    # 新版本授信流程
    QUERY_CONTACT_INFO = "sevend/query_contact_info"
    CONTACT_INFO_SUBMIT = "sevend/contact_info_submit"
    CREDIT_JOB_INFO_SUBMIT = "sevend/credit_job_info_submit"
    QUERY_CERTIFICATION_INFO = "sevend/query_certification_info"
    CHECK_ID_CARD = "sevend/check_id_card"
    GET_CREDIT_STEP_INFO = "sevend/get_credit_step_info"
    CREDIT_STEP_SUBMIT = "sevend/credit_step_submit"
    QUERY_BANK_INFOS = "sevend/query_bank_infos"
    QUERY_CUSTOMER_BASE_INFO = "sevend/query_customer_base_info"
    GET_QIAN_ZHAN_TOKEN = "sevend/get_qian_zhan_token"

    # 七牛
    ACCESS_QINIU_URL = "sevend/access_qiniu_url/{qiniu_key}"

    # 业主贷大额信用认证
    GET_VERIFY_TYPE_INFO = "sevend/get_verify_type_info"
    GET_CERTIFICATION_URL = "sevend/get_certification_url"
    SUMMIT_DRIVING_INFO = "sevend/submit_driving_info"
    GET_DRIVING_INFO = "sevend/get_driving_info"
    CERTIFICATION_CALL_BACK = "sevend/credit_call_back" # 认证状态通知接口
    CERTIFICATION_RETURN_CALL_BACK = "sevend/credit_return_call_back"# 云信退回时回调此接口
    CERTIFICATION_RESULT_CALL_BACK = "sevend/credit_result_call_back"# 云信审批完成时回调此接口
    SUBMIT_CREDIT_INFO = "sevend/submit_credit_info" # 大额步骤页信息提交接口
    # 业主贷视屏面签
    PUSH_VIDEO_SIGNATURE_RESULT = "sevend/push_video_signature_result"# 推送视屏面签结果
    GET_VIDEO_SIGNATURE_INFO = "sevend/get_video_signature_info"# 获取accid和token

    HOUSEHOLDER_LOAN_TYPE         = "sevend/householder_loan_type" # 业主贷支持的借款信息
    HOUSEHOLDER_LOAN_PURPOSE      = "sevend/householder_loan_purpose" # 贷款用途
    GET_LOAN_PURPOSE_LIST         = "sevend/get_loan_purpose_list" # 贷款用途
    SUBMIT_QUOTA_APPLY            = "sevend/submit_quota_apply" # 提交额度申请
    GET_QUOTA_APPLY_INFO          = "sevend/get_quota_apply_info" # 查看额度申请
    HOUSEHOLDER_LOAN_SUPPORT_CITY = "sevend/householder_loan_support_city" # 业主贷支持的城市
    GET_CUSTOMER_CREDIT_STEP      = "sevend/get_customer_credit_step" # 获取用户授信步骤页
    GET_IDENTITY_INFO_STATUS      = "sevend/get_identity_info_status" # 身份信息状态

    GET_IDCARD_INFO = "sevend/get_idcard_info" # 查询身份证信息
    SUBMIT_IDCARD = "sevend/submit_idcard" # 提交身份证信息
    SUBMIT_FACE_INFO = "sevend/face_url_info_submit" # 提交人脸

    GET_JOB_INFO = "sevend/get_job_info" # 查询工作信息
    SUBMIT_COMPANY_INFO = "sevend/submit_company_info" # 查询工作信息
    SUBMIT_JOB_INFO = "sevend/submit_job_info" # 提交工作信息

    QUERY_FACE_AUTH_RESULT = "sevend/query_face_auth_status" # 查询人脸认证状态

    GET_HEADSHIP_LIST = "sevend/get_headship_list" # 获取职务列表
    GET_COMPANY_NATURE_LIST = "sevend/get_company_nature_list" # 获取公司性质列表
    GET_INDUSTRY_CATEGORY_LIST = "sevend/get_industry_category_list" # 获取所属行业列表

    GET_PERSONAL_INFO = "sevend/get_personal_info" # 获取个人信息
    SUBMIT_PERSONAL_INFO = "sevend/submit_personal_info" # 提交个人信息
    GET_MARITAL_STATUS_LIST = "sevend/get_marital_status_list" # 获取婚姻状况
    GET_EDUCATION_LIST = "sevend/get_education_list" # 获取学历列表
    GET_ESTATE_SITUATION_LIST = "sevend/get_estate_situation_list" # 获取居住状况列表

    GET_CONTACT_INFO = "sevend/get_contact_info" # 获取联系人信息
    SUBMIT_CONTACT_INFO = "sevend/submit_contact_info" # 提交联系人信息

    GET_ESTATE_TYPE_LIST = "sevend/get_estate_type_list" # 房产类型
    GET_ESTATE_LOAN_TYPE_LIST = "sevend/get_estate_loan_type_list" # 业主贷款状态
    GET_ESTATE_OWNER_LIST = "sevend/get_estate_owner_list" # 房产归属

    GET_ESTATE_INFO_LIST = "sevend/get_estate_list" # 获取房产列表
    GET_ESTATE_DETAIL = "sevend/get_estate_detail" # 获取房产详情
    SUBMIT_ESTATE_INFO = "sevend/submit_estate_info" # 提交房产信息
    DELETE_ESTATE_INFO = "sevend/delete_estate_info" # 删除房产信息

    QUERY_ADDITIONAL_INFO = "sevend/query_additional_info" # 查询退补件
    SUBMIT_ADDITIONAL_INFO = "sevend/submit_additional_info" # 提交退补件资料

    HOUSEHOLDER_LOAN_MONTHLY_REPAY = "sevend/householder_loan_monthly_repay" # 业主贷预计月供

    GET_TEXT_BY_CODE = "sevend/get_text_by_code" # 根据业务类型拉取文案

    ADD_DX_WHITE_LIST = "sevend/add_dx_white_list" # 添加电销白名单

    # 保证金接口
    GET_BOND_LOAN_LIMIT = "sevend/get_bond_loan_limit"
    CALC_BOND_REPAY_PLAN = "sevend/calc_bond_repay_plan"
    SEND_BOND_LOAN_SMS = "sevend/send_bond_loan_sms"
    GET_BOND_LOAN_PROTOCOL = "sevend/get_bond_loan_protocol"
    CONFIRM_BOND_LOAN = "sevend/confirm_bond_loan"
    GET_BOND_DETAIL = "sevend/get_bond_detail"
    SEND_BOND_WITHHOLD_SMS = "sevend/send_bond_withhold_sms"
    CONFIRM_BOND_WITHHOLD = "sevend/confirm_bond_withhold"

    # 获取增值包分级
    GET_EXTRA_FEE_RANGE = "sevend/get_extra_fee_range"

    LOAN_RETURN_NOTIFY = "sevend/loan_return_notify"

    REPAY_CALLBACK = "sevend/repay_callback"

    # 活体认证
    GET_LIVING_AUTHENTICATION_SUPPLIER = "sevend/authentication/living_supplier" # 活体认证供应商，用户比例
    GET_KYC_TICKET = "sevend/authentication/kyc_ticket" # kyc信息
    GET_KYC_SUBMIT = "sevend/authentication/kyc_submit" # kyc结果提交

    # 批量用户冻结
    BATCH_CUSTOMER_FROZEN = "sevend/batch_customer_frozen"
    # 批量小额用户提额
    BATCH_SMALL_CONSUMER_INCREASE = "sevend/batch_small_consumer_increase"

    #获取贷款用途图片
    GET_LOAN_PURPOSE_IMAGE = "sevend/get_loan_purpose_image"

    #提交贷款用途图片
    SUBMIT_LOAN_PURPOSE_IMAGE = "sevend/submit_loan_purpose_image"

