from connection import Database
from pandas import read_excel, read_sql 
import os 
from config_db import Config
import datetime 

db = Database(Config)


class ProcessingFileANS:

    def read_data_excel(self, path):
        if os.name == 'nt':
           bar = '\\'
        elif os.name == 'posix':
           bar = '/'
        listdir = os.listdir(path)
        path = path+bar+listdir[-1]
        print('path', path)
        for root, dirs, files in os.walk(path):
            path = root=+bar+''.join(files)

        return read_excel(path)
        

    def insert_table(self, DF, path):
        SQLString = ''
        try:
            """today = datetime.date.today()
            day = 1
            predecessor_month = (today.month - 1) % 12
            predecessor_year = today.year + ((today.month -1) // 12)

            last_month = datetime.date(predecessor_year, predecessor_month, day)"""

            listdir = os.listdir(path)
            i = listdir[-1]
            datesDir = i[13:20]+'-01'
            datesDir = datesDir.replace('_', '-')

            DF['COMPETENCIA'] = datesDir
            DF['BENEFICIARIO_ID'] = DF.index
            DF['CONFERENCIA_ID'] = DF.index


            DF['CD_MUNICIPIO'].fillna(0, inplace=True)
            DF['NUMERO'].fillna(0, inplace=True)
            DF['LOGRADOURO'].fillna('nan', inplace=True)
            DF['BAIRRO'].fillna('nan', inplace=True)
            DF['COMPLEMENTO'].fillna('nan', inplace=True)
            DF['CD_MUNICIPIO_RESIDENCIA'].fillna(0, inplace=True)
            DF['CCO_BENEFICIARIO_TITULAR'].fillna(0, inplace=True)
            DF['CNPJ_EMPRESA_CONTRATANTE'].fillna(0, inplace=True)
            DF['CPF'].fillna(0, inplace=True)
            DF['CNS'].fillna(0, inplace=True)
            DF['CEP'].fillna(0, inplace=True)
            DF['RESIDE_EXTERIOR'].fillna(0, inplace=True)
            DF['NR_PLANO_ANS'].fillna(0 , inplace=True)
            DF['REL_DEPEND'].fillna(0 , inplace=True)
            DF['MTV_CANCELAMENTO'].fillna(0, inplace=True)





            DF['DT_ATUALIZACAO'] = '20'+DF['DT_ATUALIZACAO'].str[6:9]+'-'+DF['DT_ATUALIZACAO'].str[3:5]+'-'+DF['DT_ATUALIZACAO'].str[0:2]
            DF['DT_NASCIMENTO'] = '20'+DF['DT_NASCIMENTO'].str[6:9]+'-'+DF['DT_NASCIMENTO'].str[3:5]+'-'+DF['DT_NASCIMENTO'].str[0:2]
            DF['DT_CANCELAMENTO'] = '20'+DF['DT_CANCELAMENTO'].str[6:9]+'-'+DF['DT_CANCELAMENTO'].str[3:5]+'-'+DF['DT_CANCELAMENTO'].str[0:2]
            DF['DT_CONTRATACAO'] = '20'+DF['DT_CONTRATACAO'].str[6:9]+'-'+DF['DT_CONTRATACAO'].str[3:5]+'-'+DF['DT_CONTRATACAO'].str[0:2]
            for i in range(len(DF)):
                BAIRRO = str(DF.BAIRRO[i].replace("'", ''))
                LOGRADOURO = str(DF.LOGRADOURO[i].replace("'", ''))
                COMPLEMENTO = str(DF.COMPLEMENTO[i].replace("'", ''))
                
                SQL = (f'''EXEC SP_INSERT_BENEFICIARIOANS @p_BENEFICIARIO_ID= '{DF.BENEFICIARIO_ID[i]}',
                                                    @p_CCO= '{DF.CCO[i]}',
                                                    @p_SITUACAO= '{DF.SITUACAO[i]}' ,
                                                    @p_dataAtualizacao= '{DF.DT_ATUALIZACAO[i]}',
                                                    @p_CONFERENCIA_ID= '{DF.CONFERENCIA_ID[i]}',
                                                    @p_LOGRADOURO= '{LOGRADOURO}',
                                                    @p_NUMERO= '{DF.NUMERO[i]}',
                                                    @p_COMPLEMENTO= '{COMPLEMENTO}',
                                                    @p_BAIRRO= '{BAIRRO}',
                                                    @p_codigoMunicipio= {DF.CD_MUNICIPIO[i]},
                                                    @p_codigoMunicipioResidencia= {DF.CD_MUNICIPIO_RESIDENCIA[i]},
                                                    @p_CEP= {DF.CEP[i]},
                                                    @p_resideExterior= {DF.RESIDE_EXTERIOR[i]},
                                                    @p_tipoEndereco= '{DF.TP_ENDERECO[i]}',
                                                    @p_CPF= {DF.CPF[i]},
                                                    @p_CNS= {DF.CNS[i]},
                                                    @p_NOME= '{DF.NOME[i]}',
                                                    @p_SEXO= '{DF.SEXO[i]}',
                                                    @p_dataNascimento= '{DF.DT_NASCIMENTO[i]}',
                                                    @p_nomeMae= '{DF.NOME_MAE[i]}',
                                                    @p_ccoBeneficiarioTitular= {DF.CCO_BENEFICIARIO_TITULAR[i]},
                                                    @p_cnpjEmpresaContratante= {DF.CNPJ_EMPRESA_CONTRATANTE[i]},
                                                    @p_codigoBeneficiario= '{DF.CD_BENEFICIARIO[i]}',
                                                    @p_dataCancelamento= '{DF.DT_CANCELAMENTO[i]}',
                                                    @p_datacontratacao= '{DF.DT_CONTRATACAO[i]}',
                                                    @p_itensExcluidosCobertura= '{DF.ITENS_EXCLUIDOS_COBERTURA[i]}',
                                                    @p_motivoCancelamento= {DF.MTV_CANCELAMENTO[i]},
                                                    @p_numeroPlanoANS= {DF.NR_PLANO_ANS[i]},
                                                    @p_relacaoDependencia= {DF.REL_DEPEND[i]},
                                                    @p_COMPETENCIA= '{DF.COMPETENCIA[i]}' ''')
                #print(SQL)
                SQLString = SQL
                db.execute(SQL)
        except Exception as e:
            print(SQLString, e)
            db.rollback()
        finally:    
            db.commit()
            db.__disconnect__()


    def DoStart(self, path):
        try:
            #get date filename and check if exists competencia 
            listdir = os.listdir(path)
            i = listdir[-1]
            datesDir = i[13:20]+'-01'
            datesDir = datesDir.replace('_', '-')

            sql = (f'''SELECT * FROM BENEFICIARIOANS WHERE COMPETENCIA = '{datesDir}' ''')
            DF = read_sql(sql, db.open_connection())
            print(sql, path)
            if DF.empty:
                self.insert_table(self.read_data_excel(path), path)
                
            else:
                print('Competencia já existe!')
        except Exception as e:
            print(e)



