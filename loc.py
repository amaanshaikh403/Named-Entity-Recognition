import nltk

def stem(pattern):
    pattern={
        #uuru
        (r'.*uuru$','LOC'),
        (r'.*uuriMda$','LOC'),
        (r'.*uurige$','LOC'),
        (r'.*uurannu$','LOC'),
        (r'.*uuralli$','LOC'),
        (r'.*uurinalli$','LOC'),
        (r'.*uurinallida$','LOC'),
        (r'.*uuriniMda$','LOC'),
        (r'.*uurinavarege$','LOC'),
        (r'.*uurinallittu$','LOC'),
        (r'.*uurallittu$','LOC'),

        #pura
        (r'.*pura$','LOC'),
        (r'.*purige$','LOC'),
        (r'.*puradiMda$','LOC'),
        (r'.*puradalli$','LOC'),
        (r'.*puravannu$','LOC'),
        (r'.*purada$','LOC'),
        (r'.*puradavarege$','LOC'),
        (r'.*puradalliyavarege$','LOC'),
        (r'.*purudallittu$','LOC'),
        
        #nagara
        (r'.*nagara$','LOC'),
        (r'.*nagaradalli$','LOC'),
        (r'.*nagaravannu$','LOC'),
        (r'.*nagarige$','LOC'),
        (r'.*nagaradiMda$','LOC'),
        (r'.*nagarada$','LOC'),
        (r'.*nagaradavarege$','LOC'),
        (r'.*nagaradalliyavarege$','LOC'),
        (r'.*nagaradallittu$','LOC'),

        #paaLya
        (r'.*paaLya$','LOC'),
        (r'.*paaLyadalli$','LOC'),
        (r'.*paaLyage$','LOC'),
        (r'.*paaLyadiMda$','LOC'),
        (r'.*paaLyavannu$','LOC'),
        (r'.*paaLyadalliyavarege$','LOC'),
        (r'.*paaLyada$','LOC'),
        (r'.*paaLyadavarege$','LOC'),
        (r'.*paaLyadallittu$','LOC'),

        #gaD,raayagaDh,jaigaD,deevgaDda
        (r'.*gaD$','LOC'),
        (r'.*gaDi$','LOC'),
        (r'.*gaDh$','LOC'),
        (r'.*gaDiyiMda$','LOC'),
        (r'.*gaDiyannu$','LOC'),
        (r'.*gaDda$','LOC'),
        (r'.*gaDiyalli$','LOC'),
        (r'.*gaDige$','LOC'),
        (r'.gadiyavarege$','LOC'),
        (r'.*gaDhda$','LOC'),
        (r'.*gaDhdalli$','LOC'),
        (r'.*gaDhdiMda$','LOC'),
        (r'.*gaDdalli$','LOC'),
        (r'.*gaDdiMda$','LOC'),
        (r'.*gaDiyalliyavarege$','LOC'),
        (r'.*gaDhdavarege$','LOC'),
        (r'.*gaDhdalliyavarege$','LOC'),
        (r'.*gaDhdage$','LOC'),
        (r'.*gaDillittu$','LOC'),
        (r'.*gaDiyallittu$','LOC'),
        (r'.*gaDhdallittu$','LOC'),
        (r'.*gaDdallittu$','LOC'),

        #gal,kuNigal,gujigal
        (r'.*gal$','LOC'),
        (r'.*gallli$','LOC'),
        (r'.*galiMda','LOC'),
        (r'.*galannu$','LOC'),
        (r'.*gallige$','LOC'),
        (r'.*gallliyavarege$','LOC'),
        (r'.*galllittu$','LOC'),
        
        #haLLi
        (r'.*haLLi$','LOC'),
        (r'.*haLLiyalli$','LOC'),
        (r'.*haLLiyiMda$','LOC'),
        (r'.*haLLiyannu$','LOC'),
        (r'.*haLLige$','LOC'),
        (r'.*halliyavarege$','LOC'),
        (r'.*haLLiyallittu$','LOC'),

        #pradheesha
        (r'.*pradheesha$','LOC'),
        (r'.*pradheeshada$','LOC'),
        (r'.*pradheeshadalli$','LOC'),
        (r'.*pradheeshadiMda$','LOC'),
        (r'.*pradheeshavannu$','LOC'),
        (r'.*pradheeshadavarege$','LOC'),
        (r'.*pradheeshadalliyavarege$','LOC'),
        (r'.*pradheeshadallittu$','LOC'),

        #saagara
        (r'.*saagara$','LOC'),
        (r'.*saagaravannu$','LOC'),
        (r'.*saagaradiMda$','LOC'),
        (r'.*saagaradalli$','LOC'),
        (r'.*saagaradavarege$','LOC'),
        (r'.*saagaradalliyavarege$','LOC'),
        (r'.*saagarige$','LOC'),
        (r'.*sagaradallige$','LOC'),
        (r'.*sagaradallittu$','LOC'),
        

        #giri
        (r'.*giri$','LOC'),
        (r'.*giriyalli$','LOC'),
        (r'.*giriyiMda$','LOC'),
        (r'.*girige$','LOC'),
        (r'.*giriyavarege$','LOC'),

        #raashTra
        (r'.*raashTra$','LOC'),
        (r'.*raashTrada$','LOC'),
        (r'.*raashTradalli$','LOC'),
        (r'.*raashTravannu$','LOC'),
        (r'.*raashTradalliyavarege$','LOC'),
        (r'.*raashTrage$','LOC'),
        (r'.*raashTradallittu$','LOC'),
        (r'.*raashTradiMda$','LOC'),
        (r'.*raashTradavarege$','LOC'),

        #
        }
    return pattern
