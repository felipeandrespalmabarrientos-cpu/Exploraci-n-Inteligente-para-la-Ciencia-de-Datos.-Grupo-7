"""Funciones reutilizables para el EDA descriptivo de Fase 1."""
from pathlib import Path
import hashlib
import pandas as pd

COLUMNAS = ['survived','pclass','sex','age','sibsp','parch','fare','embarked','class','who','adult_male','deck','embark_town','alive','alone']
NUMERICAS = ['age','fare','sibsp','parch']

def cargar_datos(ruta):
    ruta = Path(ruta)
    df = pd.read_csv(ruta)
    assert list(df.columns) == COLUMNAS, 'Estructura inesperada'
    assert df.shape == (891,15), 'Dimensiones inesperadas'
    assert df.survived.notna().all() and df.survived.isin([0,1]).all()
    assert df.pclass.isin([1,2,3]).all()
    assert not df[['age','fare']].lt(0).any().any()
    df['class'] = pd.Categorical(df['class'], categories=['First','Second','Third'], ordered=True)
    df['deck'] = pd.Categorical(df['deck'], categories=list('ABCDEFG'))
    return df

def huella(ruta):
    return hashlib.sha256(Path(ruta).read_bytes()).hexdigest()

def calidad(df):
    return pd.DataFrame({'tipo':df.dtypes.astype(str),'nulos':df.isna().sum(),'porcentaje_nulos':(df.isna().mean()*100).round(2),'valores_unicos':df.nunique()}).sort_values('nulos',ascending=False)

def derivar(df):
    resultado = df.copy(deep=True)
    resultado['familia_a_bordo'] = resultado.sibsp + resultado.parch + 1
    resultado['viaja_solo'] = resultado.familia_a_bordo.eq(1)
    pd.testing.assert_frame_equal(resultado[df.columns],df)
    assert resultado.viaja_solo.eq(resultado.alone).all()
    return resultado

def resumen_grupo(df, columnas):
    return (df.groupby(columnas,dropna=False,observed=True)['survived'].agg(n='size',sobrevivientes='sum',tasa='mean').assign(tasa_pct=lambda x:(100*x.tasa).round(2)))

def frecuencias(serie):
    return pd.DataFrame({'n':serie.value_counts(dropna=False),'porcentaje':(serie.value_counts(dropna=False,normalize=True)*100).round(2)})

def outliers_iqr(serie):
    q1,q3 = serie.quantile([.25,.75]); iqr=q3-q1
    li,ls=q1-1.5*iqr,q3+1.5*iqr
    mask=serie.lt(li)|serie.gt(ls)
    return {'n_validos':int(serie.notna().sum()),'q1':q1,'q3':q3,'iqr':iqr,'limite_inferior':li,'limite_superior':ls,'n_atipicos':int(mask.sum()),'pct_validos':round(100*mask.sum()/serie.notna().sum(),2)}
