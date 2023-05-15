from modeltranslation.translator import translator, TranslationOptions
from .models import Course, Video, OrderItem, Category, Technology, Country,Language, Button, City



class CourseTranslationOptions(TranslationOptions):
    fields = ('name_of_product', 'slug')

translator.register(Course, CourseTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)


class TechnologyTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Technology, TechnologyTranslationOptions)


class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Country, CountryTranslationOptions)


class LanguageTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Language, LanguageTranslationOptions)


class ButtonTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Button, ButtonTranslationOptions)


class CityTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(City, CityTranslationOptions)

