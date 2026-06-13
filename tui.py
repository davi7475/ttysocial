from dialog import Dialog
class TUI:
    def texto(texto):
        dg = Dialog(dialog="dialog")
        dg.msgbox(text=texto, height=0, width=0)
        dg.clear()
    def entrada_linha_obrigatoria(pergunta):
        entrada = True
        dg = Dialog(dialog="dialog")
        while entrada == True:
            code, text = dg.inputbox(text=pergunta, height=0, width=0)
            if code == dg.OK:
                entrada = False
                return text
        dg.clear()
    def entrada_linha(pergunta):
        dg = Dialog(dialog="dialog")
        code, text = dg.inputbox(pergunta, height=0, width=0)
        if code == dg.OK:
            entrada = False
            return text
        dg.clear()
    def menu(menu):
        dg = Dialog(dialog="dialog")
        code, tag = dg.menu("Escolha uma opção:", choices=menu, width=0, height=0)
        if code == dg.OK:
            return str(tag)
        dg.clear()
    def entrada_multilinha(texto_inicial):
        obrigar = True
        while obrigar == True:
            dg = Dialog(dialog="dialog")
            codigo, resposta = dg.editbox_str(texto_inicial)
            obrigar = False
            return resposta
            dg.clear()