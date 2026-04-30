from flask import Flask, render_template

app = Flask(__name__)

# Link do WhatsApp Centralizado com seu número de Nova Odessa
WHATSAPP_LINK = "https://wa.me/5519983516925?text=Olá%20André,%20vi%20seu%20site%20e%20gostaria%20de%20mais%20informações."

@app.route('/')
def index():
    servicos = [
        {"titulo": "Automação de Processos", "desc": "Criação de scripts em Python para eliminar tarefas repetitivas e erros manuais."},
        {"titulo": "Gestão de Dados", "desc": "Organização de planilhas complexas, conversão de arquivos e geração de relatórios automáticos."},
        {"titulo": "Suporte Administrativo", "desc": "Auxílio em rotinas de escritório, elaboração de documentos e organização digital."},
        {"titulo": "RPA (Robôs de Processo)", "desc": "Desenvolvimento de robôs para execução de tarefas em sistemas web e desktop."}
    ]
    return render_template('index.html', servicos=servicos, whatsapp=WHATSAPP_LINK)

@app.route('/certificados')
def certificados():
    # Liste aqui seus certificados reais. O campo 'arquivo' deve ser o nome da imagem na pasta static/img
    meus_certificados = [
        {
            "titulo": "Técnico em Informática", 
            "info": "Formação técnica profissionalizante completa.",
            "arquivo": "tecnico_info.png" 
        },
        {
            "titulo": "Python para Automação", 
            "info": "Especialização em scripts, automação de tarefas e RPA.",
            "arquivo": "python.jpg"
        },
        {
            "titulo": "Excel Avançado", 
            "info": "Domínio em fórmulas complexas e tratamento de dados.",
            "arquivo": "excel.jpg"
        }
    ]
    return render_template('certificados.html', lista=meus_certificados, whatsapp=WHATSAPP_LINK)

if __name__ == '__main__':
    app.run(debug=True)