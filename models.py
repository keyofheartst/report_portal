# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Certificate(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    accountid = models.CharField(db_column='ACCOUNTID', max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    accountemail = models.CharField(db_column='ACCOUNTEMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SERIALNUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectdn = models.CharField(db_column='SUBJECTDN', max_length=500, blank=True, null=True)  # Field name made lowercase.
    issuerdn = models.CharField(db_column='ISSUERDN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validfrom = models.DateTimeField(db_column='VALIDFROM', blank=True, null=True)  # Field name made lowercase.
    validto = models.DateTimeField(db_column='VALIDTO', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    workername = models.CharField(db_column='WORKERNAME', max_length=50)  # Field name made lowercase.
    certbase64 = models.TextField(db_column='CERTBASE64', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
    activedtime = models.DateTimeField(db_column='ACTIVEDTIME', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CERTIFICATE'


class Systemconfig(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    configgroup = models.CharField(db_column='CONFIGGROUP', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    configkey = models.CharField(db_column='CONFIGKEY', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=500, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SYSTEMCONFIG'


class Transaction(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FILEPATH', max_length=100, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=1000)  # Field name made lowercase.
    filecontenttype = models.CharField(db_column='FILECONTENTTYPE', max_length=150, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    fileextension = models.CharField(db_column='FILEEXTENSION', max_length=10, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    filesize = models.CharField(db_column='FILESIZE', max_length=10, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    trantype = models.CharField(db_column='TRANTYPE', max_length=10, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    certid = models.CharField(db_column='CERTID', max_length=36, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    certsubjectdn = models.CharField(db_column='CERTSUBJECTDN', max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='ACCOUNTID', max_length=36, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    receiverid = models.CharField(db_column='RECEIVERID', max_length=36, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    tranferdate = models.DateTimeField(db_column='TRANFERDATE', blank=True, null=True)  # Field name made lowercase.
    approvedate = models.DateTimeField(db_column='APPROVEDATE', blank=True, null=True, db_comment='Ngay phe duyet')  # Field name made lowercase.
    message = models.CharField(db_column='MESSAGE', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    receivertranid = models.CharField(db_column='RECEIVERTRANID', max_length=36, blank=True, null=True, db_comment='Tranid cua nguoi nhan')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRANSACTION'


class TClaimSummary(models.Model):
    loaihinh_bh = models.CharField(max_length=100, blank=True, null=True)
    phongban = models.CharField(max_length=500, blank=True, null=True)
    sodon = models.CharField(max_length=60, blank=True, null=True)
    tenkh = models.CharField(max_length=1000, blank=True, null=True)
    policy_version = models.CharField(max_length=100, blank=True, null=True)
    doituongbh = models.CharField(max_length=1000, blank=True, null=True)
    ma_nvu = models.CharField(max_length=60, blank=True, null=True)
    ngaycapdon = models.DateField(blank=True, null=True)
    nhanvien = models.CharField(max_length=500, blank=True, null=True)
    accmonth = models.DateField(blank=True, null=True)
    inception_date = models.DateField(blank=True, null=True)
    maturity_date = models.DateField(blank=True, null=True)
    suminsure = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    claim_folder_number = models.CharField(max_length=100, blank=True, null=True)
    claim_offer_number = models.CharField(max_length=100, blank=True, null=True)
    loai_tien_ngte = models.CharField(max_length=100, blank=True, null=True)
    tien_bt = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    boithuong_vnd = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ty_gia = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    loss_type_name = models.CharField(max_length=1500, blank=True, null=True)
    ngayboithuong = models.DateField(blank=True, null=True)
    ngaytonthat = models.DateField(blank=True, null=True)
    ngaythongbaott = models.DateField(blank=True, null=True)
    tien_gd = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuongtbh_nn = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuongtbh_vn = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    thugiambt = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    btthuoctngl = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_fac = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_qs = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_sp = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_xol = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ky_tt = models.DateField(blank=True, null=True)
    congty_giamdinh = models.CharField(max_length=300, blank=True, null=True)
    congtytpa = models.CharField(max_length=1000, blank=True, null=True)
    mamoigioi = models.CharField(max_length=100, blank=True, null=True)
    madaily = models.CharField(max_length=100, blank=True, null=True)
    tenmoigioi = models.CharField(max_length=1000, blank=True, null=True)
    tendaily = models.CharField(max_length=1000, blank=True, null=True)
    tyle_dbh = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tyle_nt = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    cause_of_loss = models.CharField(max_length=1500, blank=True, null=True)
    detail_loss = models.CharField(max_length=1500, blank=True, null=True)
    leader = models.CharField(max_length=1000, blank=True, null=True)
    don_goc = models.CharField(max_length=100, blank=True, null=True)
    company_id = models.CharField(max_length=100, blank=True, null=True)
    department_id = models.CharField(max_length=100, blank=True, null=True)
    underwriter_id = models.CharField(max_length=100, blank=True, null=True)
    product_group_id = models.CharField(max_length=100, blank=True, null=True)
    broker_id = models.CharField(max_length=100, blank=True, null=True)
    agent_id = models.CharField(max_length=100, blank=True, null=True)
    tpa_id = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CLAIM_SUMMARY'


class TSummaryRevenue(models.Model):
    loai_hinh_bh = models.CharField(max_length=100, blank=True, null=True)
    phong = models.CharField(max_length=300, blank=True, null=True)
    so_don = models.CharField(max_length=100, blank=True, null=True)
    ma_nghiepvu = models.CharField(max_length=100, blank=True, null=True)
    acc_month = models.DateField(blank=True, null=True)
    ky_tt = models.DateField(blank=True, null=True)
    ngay_thanh_toan_phibh = models.DateField(blank=True, null=True)
    ten_kh = models.CharField(max_length=300, blank=True, null=True)
    doituongbh = models.CharField(max_length=300, blank=True, null=True)
    phi_bh_nte = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phi_bh_bb = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    loai_tien_nte = models.CharField(max_length=100, blank=True, null=True)
    ty_gia = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phibh_vnd = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    vat_vnd = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ngay_capdon = models.DateField(blank=True, null=True)
    nhanvien = models.CharField(max_length=300, blank=True, null=True)
    inception_date = models.DateField(blank=True, null=True)
    maturity_date = models.DateField(blank=True, null=True)
    si_vnd = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    broker_id = models.CharField(max_length=100, blank=True, null=True)
    broker_rate = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    agent_id = models.CharField(max_length=100, blank=True, null=True)
    hoahong_dl = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    chiphi_dbh = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    congtytpa = models.CharField(max_length=300, blank=True, null=True)
    sotientpa = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phicapdon = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phi_bh_bb_vnd = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_tbh_vn = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_tbh_hh_vn = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_tbh_nn = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_tbh_hh_nn = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nhuong_tbh_thue_nn = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phi_elc = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    loai_hd = models.CharField(max_length=100, blank=True, null=True)
    phi_giulai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ty_le_tn_giu_lai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ghichu = models.CharField(max_length=1000, blank=True, null=True)
    ty_le_fac = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phi_fac = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hoa_hong_fac = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ty_le_qs = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phi_qs = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hoa_hong_qs = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ty_le_sp = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phi_sp = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hoa_hong_sp = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ty_le_eol = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    phitailapxol = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    new_renew = models.CharField(max_length=100, blank=True, null=True)
    tyle_dbh = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tyle_nt = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    re_status = models.CharField(max_length=100, blank=True, null=True)
    product_group_id = models.CharField(max_length=100, blank=True, null=True)
    product_coverage_id = models.CharField(max_length=100, blank=True, null=True)
    issue_premium_rate = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    don_goc = models.CharField(max_length=100, blank=True, null=True)
    policy_version = models.CharField(max_length=100, blank=True, null=True)
    retention_pre = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hoa_hong_elc = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    company_id = models.CharField(max_length=100, blank=True, null=True)
    department_id = models.CharField(max_length=100, blank=True, null=True)
    underwriter_id = models.CharField(max_length=100, blank=True, null=True)
    tpa_id = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_SUMMARY_REVENUE'


class UicCertificate(models.Model):
    cert_id = models.CharField(db_column='CERT_ID', primary_key=True, max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    accountid = models.CharField(db_column='ACCOUNTID', max_length=50, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    accountemail = models.CharField(db_column='ACCOUNTEMAIL', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SERIALNUMBER', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    subjectdn = models.CharField(db_column='SUBJECTDN', max_length=500, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    issuerdn = models.CharField(db_column='ISSUERDN', max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    validfrom = models.DateTimeField(db_column='VALIDFROM', blank=True, null=True)  # Field name made lowercase.
    validto = models.DateTimeField(db_column='VALIDTO', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=2, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    workername = models.CharField(db_column='WORKERNAME', max_length=50, db_collation='utf8mb3_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    certbase64 = models.TextField(db_column='CERTBASE64', db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
    activedtime = models.DateTimeField(db_column='ACTIVEDTIME', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIC_CERTIFICATE'


class UicDepartment(models.Model):
    dept_id = models.CharField(db_column='DEPT_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIC_DEPARTMENT'


class UicSignatureTransaction(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FILEPATH', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=1000, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    filecontenttype = models.CharField(db_column='FILECONTENTTYPE', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    fileextension = models.CharField(db_column='FILEEXTENSION', max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    filesize = models.CharField(db_column='FILESIZE', max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    trantype = models.CharField(db_column='TRANTYPE', max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    certid = models.CharField(db_column='CERTID', max_length=36, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    certsubjectdn = models.CharField(db_column='CERTSUBJECTDN', max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='ACCOUNTID', max_length=36, db_collation='utf8mb3_general_ci', blank=True, null=True, db_comment='Uploader')  # Field name made lowercase.
    receiverid = models.CharField(db_column='RECEIVERID', max_length=36, db_collation='utf8mb3_general_ci', blank=True, null=True, db_comment='Sub Signer')  # Field name made lowercase.
    tranferdate = models.DateTimeField(db_column='TRANFERDATE', blank=True, null=True)  # Field name made lowercase.
    approvedate = models.DateTimeField(db_column='APPROVEDATE', blank=True, null=True, db_comment='Ngay phe duyet')  # Field name made lowercase.
    message = models.CharField(db_column='MESSAGE', max_length=5000, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    receivertranid = models.CharField(db_column='RECEIVERTRANID', max_length=36, db_collation='utf8mb3_general_ci', blank=True, null=True, db_comment='Main Signer')  # Field name made lowercase.
    flow_id = models.CharField(db_column='FLOW_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    worker_signer = models.CharField(db_column='WORKER_SIGNER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    updater_id = models.CharField(db_column='UPDATER_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIC_SIGNATURE_TRANSACTION'


class UicSignWorkFlowGroup(models.Model):
    group_id = models.CharField(db_column='GROUP_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    group_flow_name = models.CharField(db_column='GROUP_FLOW_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dept_id = models.CharField(db_column='DEPT_ID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    signer = models.CharField(db_column='SIGNER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sub_signer = models.CharField(db_column='SUB_SIGNER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE', blank=True, null=True)  # Field name made lowercase.
    creater = models.CharField(db_column='CREATER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    updater = models.CharField(db_column='UPDATER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    worker_signer = models.CharField(db_column='WORKER_SIGNER', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIC_SIGN_WORK_FLOW_GROUP'


class UicUserAccount(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=300, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    userldap = models.CharField(db_column='USERLDAP', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PHONENUMBER', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    cmnd = models.CharField(db_column='CMND', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=500, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='BIRTHDAY', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LASTLOGIN', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='MODIFIEDDATE', blank=True, null=True)  # Field name made lowercase.
    accounttype = models.IntegerField(db_column='ACCOUNTTYPE', blank=True, null=True)  # Field name made lowercase.
    otprequire = models.IntegerField(db_column='OTPREQUIRE', blank=True, null=True)  # Field name made lowercase.
    twofactortype = models.IntegerField(db_column='TWOFACTORTYPE', blank=True, null=True)  # Field name made lowercase.
    twofactorname = models.CharField(db_column='TWOFACTORNAME', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    avatar = models.TextField(db_column='AVATAR', db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    firstlogin = models.IntegerField(db_column='FIRSTLOGIN', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.IntegerField(db_column='DEPT_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIC_USER_ACCOUNT'


class UicUserCertificate(models.Model):
    user_cert_id = models.CharField(db_column='USER_CERT_ID', primary_key=True, max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    accountid = models.CharField(db_column='ACCOUNTID', max_length=50, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    cert_id = models.CharField(db_column='CERT_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    worker_name = models.CharField(db_column='WORKER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIC_USER_CERTIFICATE'


class Useraccount(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=300, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    userldap = models.CharField(db_column='USERLDAP', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PHONENUMBER', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    cmnd = models.CharField(db_column='CMND', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=500, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='BIRTHDAY', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LASTLOGIN', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='MODIFIEDDATE', blank=True, null=True)  # Field name made lowercase.
    accounttype = models.IntegerField(db_column='ACCOUNTTYPE', blank=True, null=True)  # Field name made lowercase.
    otprequire = models.IntegerField(db_column='OTPREQUIRE', blank=True, null=True)  # Field name made lowercase.
    twofactortype = models.IntegerField(db_column='TWOFACTORTYPE', blank=True, null=True)  # Field name made lowercase.
    twofactorname = models.CharField(db_column='TWOFACTORNAME', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    avatar = models.TextField(db_column='AVATAR', db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    firstlogin = models.IntegerField(db_column='FIRSTLOGIN', blank=True, null=True)  # Field name made lowercase.
    logincount = models.IntegerField(db_column='LOGINCOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERACCOUNT'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
