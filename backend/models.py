from django.db import models


# Create your models here.


class Collection(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='Фото коллекции', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название коллекции')

    # en
    name_en = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название коллекции {en}')

    # uz
    name_uz = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название коллекции {uz}')

    def __str__(self):
        return self.name

    def get_image(self):
        try:
            return self.image.url
        except:
            return ''

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Material(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название материала')

    # en
    name_en = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название материала {en}')

    # uz
    name_uz = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название материала {uz}')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Item(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название товара')
    description = models.TextField(null=True, blank=True, verbose_name='Описание товара')

    # en
    name_en = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название товара {en}')
    description_en = models.TextField(null=True, blank=True, verbose_name='Описание товара {en}')

    # uz
    name_uz = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название товара {uz}')
    description_uz = models.TextField(null=True, blank=True, verbose_name='Описание товара {uz}')

    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал товара')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Коллекция товара',
                                   related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True,
                                verbose_name='Цена товара в долларах')

    price_uz = models.CharField(max_length=150, null=True, blank=True, verbose_name='Цена в сумах')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')

    def get_image(self):
        try:
            return self.image.url
        except:
            return ''

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'


class CountBlogAbout(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок поля')
    image = models.ImageField(upload_to='images', verbose_name='Фото поля')

    def __str__(self):
        return self.title

    def get_image(self):
        try:
            return self.image.url
        except:
            return ''

    class Meta:
        verbose_name = 'Поле о нас'
        verbose_name_plural = 'Поля о нас'


class AboutUs(models.Model):
    ind = models.PositiveIntegerField(verbose_name='Индексация элемента')

    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Заголовок блока о нас')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    # en
    title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name='Заголовок блока о нас {en}')
    description_en = models.TextField(null=True, blank=True, verbose_name='Описание {en}')

    # uz
    title_uz = models.CharField(max_length=255, null=True, blank=True, verbose_name='Заголовок блока о нас {uz}')
    description_uz = models.TextField(null=True, blank=True, verbose_name='Описание {uz}')

    count = models.ForeignKey(CountBlogAbout, verbose_name='Поле информации', on_delete=models.CASCADE, null=True,
                              blank=True,
                              related_name='blogsAbout')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок о нас'
        verbose_name_plural = 'Блоки о нас'
