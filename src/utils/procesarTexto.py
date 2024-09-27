import spacy


def crearProcessing():
    nlp = spacy.load("es_core_news_sm")
    import es_core_news_sm
    nlp = es_core_news_sm.load()
    return nlp

def startProcess(nlp, text):
    doc = nlp(text)
    
    resultado = [token.lemma_.lower() for token in doc 
                 if not token.is_stop and 
                    token.is_alpha]
    return resultado

        
if __name__ == "__main__":
    nlp=crearProcessing()
    resultado=startProcess(nlp, "Ada da revisando la hora")
    print(resultado) 

else:
    pass