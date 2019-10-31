from django.contrib import admin
from .models import Despesa
import django.utils.timezone as timezone

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'tipo_despesa',
                    'descricao', 'formaDePagamento',
                    'vencimento', 'proximoVencimento', 'quitado',
                    )

    list_filter = ('quitado', 'vencimento')
    date_hierarchy = 'vencimento'

    def proximoVencimento(self, obj):
        proximo_data = timezone.localdate() + timezone.timedelta(days=2)
        print("proximo: ", proximo_data)
        print("vencimento: ", obj.vencimento)
        if proximo_data == obj.vencimento:
            return True
        else:
            return False

    proximoVencimento.short_description = "Próximo ao vencimento?"
    proximoVencimento.boolean = True


admin.site.register(Despesa, DespesaAdmin)
admin.site.site_header = "Controle de despesa"
admin.site.index_title = "Recursos"
admin.site.site_title = "Adminitração de despesas"
