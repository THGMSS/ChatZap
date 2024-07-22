# Flet -> aplicativo/site/programa de computador

import flet as ft

def main(pagina):
    
    
    # Criar o Titulo
    titulo = ft.Text("Chatzap", size= 50)
  
    def enviar_mensagem_tunel(mensagem): # Função que o túnel ira executar
           chat.controls.append(ft.Text(mensagem))
           pagina.update()
            
    pagina.pubsub.subscribe(enviar_mensagem_tunel) # Cria o túnel de comunicação
    
    
    titulo_janela = ft.Text('Bem-vindo ao chatzap')
   
    
   
    
    def enviar_mensagem(evento):
        # Enviando a mensagem no chat:
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        
        pagina.pubsub.send_all(texto) # Envia uma mensagem no túnel       
        texto_mensagem.value = ""
        pagina.add(chat)
        pagina.uptade()
    
    
    texto_mensagem = ft.TextField(label='Digite a mensagem:', on_submit= enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click =enviar_mensagem)
    
    chat = ft.Column()
    
    # colunas e linhas
    linha_mensagem=  ft.Row([texto_mensagem, botao_enviar])
   
    
    def entrar_no_chat(evento):
        # Tirando o titulo da página
        pagina.remove(titulo)
        # Tirar o botão_iniciar
        pagina.remove(botao_iniciar)
        # Fechar o popup/janela
        janela.open = False
        # Criando o chat
        # Criando o campo de texto para enviar as mensagem
        pagina.add(chat)
        pagina.add(linha_mensagem)
      
        # Escrevendo o nome do usuario no chat assim que entrar
        texto_entrou_chat = f'{campo_nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(texto_entrou_chat)
        
        
        pagina.update()
             
    campo_nome_usuario = ft.TextField(label='Escreva seu nome:', on_submit=entrar_no_chat)
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click = entrar_no_chat)
        
    janela = ft.AlertDialog (
        # Está colocando 
        title= titulo_janela,
        content=campo_nome_usuario,
        actions =[botao_entrar]         
        )
    
    
    def abrir_popup(evento): # Toda funcao que é usada dentro de um botao, tem que receber um evento como parametro
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        

    # Está criando um botão na página
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click= abrir_popup)
    
    
    # Está adicionando o titulo na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
ft.app(main, view= ft.WEB_BROWSER)