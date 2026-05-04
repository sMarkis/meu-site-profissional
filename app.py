from flask import Flask, render_template

app = Flask(__name__)

# Link do WhatsApp Centralizado
WHATSAPP_LINK = "https://wa.me/5519983516925?text=Olá%20André,%20vi%20seu%20site%20e%20gostaria%20de%20mais%20informações."

@app.route('/')
def index():
    servicos = [
        
        {"titulo": "Organização de Dados", "desc": "Limpeza e estruturação de planilhas e bancos de dados."},
        {"titulo": "Gestão de Back-Office", "desc": "Padronização de arquivos digitais e suporte interno."},
        {"titulo": "Digitalização de Documentos", "desc": "Conversão de arquivos físicos para o formato digital organizado, com foco em preservação e facilidade de busca."},
        {"titulo": "Suporte Operacional", "desc": "Relatórios, formatação técnica e controle de prazos."},
        {"titulo": "Automação de Rotinas", "desc": "Transformação de tarefas manuais repetitivas em processos digitais ágeis." },
        {"titulo": "Formatação Técnica", "desc": "Padronização de manuais, propostas e documentos conforme normas profissionais." },
        {"titulo": "Formatação de Computadores", "desc": "Instalação limpa de sistemas operacionais." },
        {"titulo": "Automação de Processos", "desc": "Criação de scripts em Python para eliminar tarefas repetitivas e erros manuais."},
        {"titulo": "Gestão de Dados", "desc": "Organização de planilhas complexas, conversão de arquivos e geração de relatórios automáticos."},
        {"titulo": "Suporte Administrativo", "desc": "Auxílio em rotinas de escritório, elaboração de documentos e organização digital."},
        {"titulo": "RPA (Robôs de Processo)", "desc": "Desenvolvimento de robôs para execução de tarefas em sistemas web e desktop."},

    ]
    return render_template('index.html', servicos=servicos, whatsapp=WHATSAPP_LINK)

@app.route('/certificados')
def certificados():
    meus_certificados = [
        {"titulo": "Técnico em Informática", "info": "Formação técnica profissionalizante completa.", "arquivo": "tecnico_info.png"},
        {"titulo": "Python para Automação", "info": "Especialização em scripts, automação de tarefas e RPA.", "arquivo": "python.jpg"},
        {"titulo": "Excel Avançado", "info": "Domínio em fórmulas complexas e tratamento de dados.", "arquivo": "excel.jpg"}
        
    ]
    return render_template('certificados.html', lista=meus_certificados, whatsapp=WHATSAPP_LINK)

@app.route('/links')
def links():
    meus_links = [
        {
            "titulo": "GitHub", 
            "info": "Repositórios de scripts Python, RPA e projetos de automação.",
            "icone": "fab fa-github",
            "url": "https://github.com/sMarkis"
        },
        {
            "titulo": "Linkedin", 
            "info": "Conexões profissionais e histórico detalhado de carreira.",
            "icone": "fab fa-linkedin",
            "url": "https://linkedin.com/in/seu-perfil"
        },
        
    ]
    return render_template('links.html', lista=meus_links, whatsapp=WHATSAPP_LINK)

if __name__ == '__main__':
    app.run(debug=True)