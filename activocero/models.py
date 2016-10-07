from django.db import models

# Create your models here.
class prog_corazon_amigo(models.Model):
    ELEGIR_GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    EDO_CIVIL = (
        ('S', 'Soltero(a)'),
        ('C', 'Casado(a)'),
        ('V', 'Viudo(a)'),
        ('D', 'Divorciado(a)'),
    )
    ESTATUS = (
        (1, 'Comite'),
        (2, 'Aprobado'),
        (3, 'No aprobado'),
        (4, 'Rechazado'),
        (5, 'Cancelado'),
        (6, 'Fallecido'),
        (7, 'Suspendido'),
        (8, 'Revalorado aprobado'),
        (9, 'Revalorado no aprobado'),
    )
    CLAVES_MUNICIPIOS = (
        (1, 'BALANCAN'),
        (2, 'CARDENAS'),
        (3, 'CENTLA'),
        (4, 'CENTRO'),
        (5, 'COMALCALCO'),
        (6, 'CUNDUACAN'),
        (7, 'EMILIANO ZAPATA'),
        (8, 'HUIMANGUILLO'),
        (9, 'JALAPA'),
        (10, 'JALPA DE MENDEZ'),
        (11, 'JONUTA'),
        (12, 'MACUSPANA'),
        (13, 'NACAJUCA'),
        (14, 'PARAISO'),
        (15, 'TACOTALPA'),
        (16, 'TEAPA'),
        (17, 'TENOSIQUE'),
    )

    FOLIO = models.IntegerField (primary_key=True, unique=True),
    CURP = models.CharField (max_length=20),
    FOLIO_ELEC = models.CharField (max_length=20),
    GRAL_OCR = models.CharField (max_length=20),
    FECINSERT = models.DateField (auto_now=True),
    FECREG = models.DateField (auto_now=True),
    FECNAC = models.DateField (auto_now=True),
    APPATERNO = models.CharField (max_length=50, default=''),
    APMATERNO = models.CharField (max_length=50, default=''),
    NOMBRE = models.CharField(max_length=50, default=''),
    SEXO = models.CharField(max_length=1, choices=ELEGIR_GENERO),
    EDOCIVIL = models.CharField(max_length=1, choices=EDO_CIVIL),
    TEL = models.CharField(max_length=20, default='0000000000'),
    ESTADO = models.CharField(max_length=2,default='27'),
    MUNICIPIO = models.IntegerField(choices=CLAVES_MUNICIPIOS),
    CVELOCAL = models.IntegerField(default=0),
    CALLEYNUM = models.CharField(max_length=100),
    REF_DIR_SOL = models.CharField(max_length=500),
    DOC_PRESENTA = models.CharField(max_length=1),
    OBS_GRAL = models.CharField(max_length=500),
    ETAPA = models.IntegerField (default=0),
    REP_APPATERNO = models.CharField(max_length=30),
    REP_APMATERNO = models.CharField(max_length=30),
    REP_NOMBRE = models.CharField(max_length=30),
    REP_SEXO = models.CharField(max_length=1, choices=ELEGIR_GENERO),
    REP_FECNAC = models.DateField(),
    REP_TEL = models.CharField(max_length=20),
    REP_MUNICIPIO = models.IntegerField (choices=CLAVES_MUNICIPIOS),
    REP_CVELOCAL = models.IntegerField(default=0),
    REP_CALLEYNUM = models.CharField(max_length=100),
    REF_DIR_REP = models.CharField(max_length=500),
    REP_DOC_PRESENTA = models.CharField(max_length=1),
    FECRECEPCION = models.DateField(),
    FECDEMANDA = models.DateField(),
    FECEVALUACION = models.DateField(),
    NOMBREDR = models.CharField(max_length=60),
    EFDESCRIP = models.CharField(max_length=500),
    DOC_SREG_O = models.CharField(max_length=1),
    REG_CRLEG_O = models.CharField(max_length=1),
    REG_EFUN_O = models.CharField(max_length=1),
    REG_TCEN_O = models.CharField(max_length=1),
    SOL_ANAC_C = models.CharField(max_length=1),
    SOL_IFE_C = models.CharField(max_length=1),
    SOL_CDOM_C = models.CharField(max_length=1),
    REP_ANAC_C = models.CharField(max_length=1),
    REP_IFE_C = models.CharField(max_length=1),
    REP_CDOM_C = models.CharField(max_length=1),
    VIV_COMPARTIDA = models.CharField(max_length=1),
    VIV_PISO = models.CharField(max_length=1),
    VIV_PAREDES = models.CharField(max_length=1, default='0'),
    VIV_TECHOS = models.CharField(max_length=1, default='0'),
    VIV_NCUARTOS = models.IntegerField(default=1),
    VIV_NCDORMIR = models.IntegerField(1),
    VIV_COCINA = models.CharField(max_length=1, default='0'),
    VIV_FOGON = models.CharField(max_length=1, default='0'),
'''
VIV_ESTUFA = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_AGUAENTUB = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_POZO = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_PIPA = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_RIOS = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_AGUAUTIL = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_DEXCRETAS = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_EBASURA = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_ELECT = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_RADIO = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_TV = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
VIV_REFRI = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_SERVSALUD = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_SEGPOP = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_NESCOLAR = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_DMOTRIZ = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_DVISUAL = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_DAUDITIVA = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_DLENGUAJE = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_DMENTAL = models.CharField(max_length=XX)(1)
DEFAULT
'0'
NOT
NULL,
EVF_DOTRA = models.CharField(max_length=XX)(100),
EVF_LALIMENTACION
Integer
NOT
NULL,
EVF_LASEOPERS
Integer
NOT
NULL,
EVF_LTRASLADO
Integer
NOT
NULL,
EVF_LCOMUNICACION
Integer
NOT
NULL,
EVF_LVESTIDO
Integer
NOT
NULL,
TH
Integer
NOT
NULL,
TM
Integer
NOT
NULL,
CNTA = models.CharField(max_length=XX)(16), \
       FECCANCEL
Timestamp,
TXTSOLMUNICIPIO = models.CharField(max_length=XX)(50),
TXTSOLLOCALIDAD = models.CharField(max_length=XX)(100),
TXTREPMUNICIPIO = models.CharField(max_length=XX)(50),
TXTREPLOCALIDAD = models.CharField(max_length=XX)(100),
LATSOL
Double
precision,
LONSOL
Double
precision,
LATREP
Double
precision,
LONREP
Double
precision,
'''
    VIV_ENCUESTADOR = models.CharField(max_length=100),
    VIV_FECENCUESTA = models.DateField(),
    MOTIVO_CANCEL = models.CharField(max_length=22),
    STATUS = models.IntegerField(max_length=1, choices=ESTATUS),
    ACOMENTARIO = models.CharField(max_length=255),
    TINCIDENCIA = models.SmallIntegerField(default='0'),
    NUMHABITANTES = models.SmallIntegerField(default='0'),
    JSUSER = models.CharField(max_length=30, default='WEBCORETI'),
    PAQUETE = models.IntegerField(),
    NOMINAID = models.IntegerField(),
    ESTUDIANTE = models.CharField(max_length=1),
    EMPLEADO = models.CharField(max_length=1),
    MESAID = models.SmallIntegerField(default='0'),
    SOL_CURP = models.CharField(max_length=1, default='0'),
    CEDULADR = models.CharField(max_length=7, default='0000000'),
    VIV_PROPIEDAD = models.CharField(max_length=1, default='0'),
    SUELDOBEN = models.DecimalField(max_digits=5, decimal_places=2, default='0.0'),
    EMPLEADOREP = models.CharField(max_length=1, default='0'),
    SUELDOREP = models.DecimalField(max_digits=5, decimal_places=2, default='0.0'),
    NOEMPLEADO = models.CharField(max_length=1, default='0'),
    VERSIONCA = models.CharField(max_length=1, default='0'),
    CUENTABANCO = models.CharField(max_length=10, default='0000000000'),
    UNIDADSALUD = models.CharField(max_length=15, default='000000000000000'),
    ACTIVO = models.CharField(max_length=1),
