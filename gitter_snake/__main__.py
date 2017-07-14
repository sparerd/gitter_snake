from ui import main
import images_rc

icons = {
    "info": ":/images/information.png",
    "exit": ":/images/door_out.png"
}

if __name__ == "__main__":
    window = main.MainWindow(icons)
    window.run()
