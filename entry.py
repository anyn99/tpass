from src.main import cli, clean_exit

import sys

def ok(x=None):
      sys.argv.extend(e.get().split())
      root.destroy()



      
if __name__ == '__main__':
      if 'idlelib.rpc' in sys.modules:
            import tkinter as tk

            root = tk.Tk()
            tk.Label(root, text="Command-line Arguments:").pack()

            e = tk.Entry(root)
            e.pack(padx=5)

            tk.Button(root, text="OK", command=ok,
                  default=tk.ACTIVE).pack(pady=5)

            root.bind("<Return>", ok)
            root.bind("<Escape>", lambda x: root.destroy())

            e.focus()
            root.wait_window()
      try:
            cli()
      except Exception as ex:
            raise ex
      finally:
            clean_exit()
