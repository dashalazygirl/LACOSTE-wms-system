from django.contrib import admin
from.models import Models_of_shoes, Arhiv, Category,Sclad


admin.site.register(Sclad)


@admin.register(Models_of_shoes)
class Models_of_shoesAdmin(admin.ModelAdmin):
    list_display = [ 'id',
                    'articul',
                    'model_s',
                    'color',
                    'short',
                    'sex',
                    'size_f',
                    'size_r',
                    'season',
                    'amount',
                    'sclad'
    ]
    list_editable = ['model_s',
                    'color',
                    'short',
                    'sex',
                    'size_f',
                    'size_r',
                    'season',
                    'amount',
                     'sclad']
    search_fields = ['sex',
                     'season',
                     'color']
    list_per_page = 10
    list_filter = ['sex',
                     'season',
                     'color']

@admin.register(Arhiv)
class ArhivAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'articul',
                    'model_s',
                    'color',
                    'short',
                    'sex',
                    'size_f',
                    'size_r',
                    'season',
                    'amount',
                    'sclad'
                    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'opisanie']


