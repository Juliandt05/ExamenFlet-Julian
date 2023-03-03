import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6

    #Fin --- Ejercicio 6


    #Ejercicio 2
    img=ft.Image(
        src=f"/fotos/Logo.png"
    )
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250
    



    tfnombre = ft.TextField(label="Nombre")
    #Ejercicio 4
    tfpassword=ft.TextField(label="Contraseña",password=True, can_reveal_password=True)

    #Fin --- Ejercicio 4


    #Ejercicio 5
    
    #Fin-- Ejercicio 5
    def comprobar(e):
        if tfnombre.value==tfpassword.value:
            dlg = ft.AlertDialog(
            title=ft.Text("La contraseña es correcta"), on_dismiss=lambda e: print("Dialog dismissed!"))
            dlg.open = True
            page.add(dlg)
            
        else:
            dlg = ft.AlertDialog(
            title=ft.Text("La contraseña es incorrecta"), on_dismiss=lambda e: print("Dialog dismissed!"))
            dlg.open = True
            page.add(dlg)
        
    btnEntrar=ft.ElevatedButton("Boton Entrar", icon="chair_outlined",on_click=comprobar)


    

    

    page.add(img,tfnombre,tfpassword,btnEntrar)
    


ft.app(target=main,assets_dir="fotos")