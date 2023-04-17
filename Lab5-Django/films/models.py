from django.db import models

class Filma(models.Model):
    izenburua = models.CharField(max_length=255)
    zuzendaria = models.CharField(max_length=255)
    urtea = models.CharField(max_length=4)
    generoa = models.CharField(max_length=2)
    sinopsia = models.TextField()
    bozkak = models.IntegerField(default=0)

    def __str__(self):
        return self.izenburua

class Bozkatzailea(models.Model):
    id = models.IntegerField(primary_key=True)
    erabiltzailea_id = models.IntegerField()


f1 = Filma(izenburua="Earthlings", zuzendaria="Shaun Monson", urtea="2005", generoa="DO", sinopsia="Using hidden cameras and never-before-seen footage, Earthlings chronicles the dayto-day practices of the largest industries in the world, all of which rely entirely on animals for profit.", bozkak="0")

f2 = Filma(izenburua="The Herd", zuzendaria="Melanie Light", urtea="2014", generoa="TH", sinopsia="Imprisoned within inhuman squalor with other women. Paula's existence and human function is abused as a resource by her captors. Escape, on any level, is hopeless as the women are condemned to a life of enforced servitude at the whims of their imprisoners for one reason only - their milk.", bozkak="0")

f3 = Filma(izenburua="Dominion", zuzendaria="Chris Delforce", urtea="2018", generoa="DO", sinopsia="Dominion uses drones, hidden and handheld cameras to expose the dark underbelly of modern animal agriculture, questioning the morality and validity of humankind's dominion over the animal kingdom. ", bozkak="0")

f4 = Filma(izenburua="Matadero: lo que la industria cárnica esconde", zuzendaria="Aitor Garmendia", urtea="2017", generoa="DO", sinopsia="El trabajo que se presenta a continuación tiene como objetivo hacer visible la explotación y violencia sistemática que padecen los animales en mataderos, la cual es mantenida oculta de forma deliberada por la industria cárnica. Con esta investigación se aporta información relevante al actual debate social y político antiespecista promovido por el movimiento de derechos animales que exige la abolición de toda explotación animal. ", bozkak="0")

f5 = Filma(izenburua="Gurean: animalien erabilera Euskal Herriko festetan", zuzendaria="Linas Korta", urtea="2018", generoa="DO", sinopsia="Askekintzak Euskal Herriko festetako animalien erabileraren inguruan inoiz egin den dokumentazio lan handiena bildu du. Gurean, 4 urteetan zehar (2014-2017) aktibista desberdinek ezkutuan grabatutako irudiekin osatutako dokumentala da.", bozkak="0")

f6 = Filma(izenburua="Hiltegiak Euskal Herrian", zuzendaria="Nor", urtea="2018", generoa="DO", sinopsia="Azken minutua: Heriotza eta erresistentzia. 3 urteetan zehar Euskal Herriko edo inguruetako hiltegietan grabatutako irudiak dira honakoak.", bozkak="0")

f7 = Filma(izenburua="Cowspiracy: The Sustainability Secret", zuzendaria="Kip Andersen eta Keegan Kuhn", urtea="2014", generoa="DO", sinopsia="Follow the shocking, yet humorous, journey of an aspiring environmentalist, as he daringly seeks to find the real solution to the most pressing environmental issues and true path to sustainability.", bozkak="0")

f8 = Filma(izenburua="Munich 1962: isildu egia", zuzendaria="Larraitz Ariznabarreta eta Naroa Anabitarte", urtea="2014", generoa="DO", sinopsia="Kezka batetik sortutako proiektua da Munich 1962: isildu egia. Ordu hartan Munichen egon zirenen hitzak jaso dituzte Orreaga Taldeko kideek. Dokumental historikoa izateaz harago doa, ikus-entzulea hausnarketara gonbidatu nahi du. 'Iruditzen zaigu oraindik ere orduan gertatutakoak gaurkotasun handia duela; oraindik berdin jarraitzen dugu, garai hartan egin ziren akats berberak errepikatzen dira gaur egun', Naroa Anabitarte (Tolosa, 1979) Orreaga Taldeko kide eta dokumentalaren egilearen esanetan. Ez du ikusten politikarien aldetik akats berak ez errepikatzeko nahirik, 'ematen du dinamika beretan jarraitu nahi dela, aldez aurretik galduak diren bideak erabiliz'.", bozkak="0")

f1.save()
f2.save()
f3.save()
f4.save()
f5.save()
f6.save()
f7.save()
f8.save()