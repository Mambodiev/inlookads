from modeltranslation.translator import translator, TranslationOptions
from .models import Course, Video, OrderItem, Category, Technology, Country,Language, Button





class CourseTranslationOptions(TranslationOptions):
    fields = ('name_of_product', 'slug')

translator.register(Course, CourseTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)