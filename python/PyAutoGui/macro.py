import pyautogui as pgui
import time
#マクロのブックをマウス選択
position=pgui.locateOnScreen('jpgbook.jpg' , confidence=0.9)
time.sleep(2)
#マクロのブックをダブルクリック
pgui.doubleClick(position)
time.sleep(2)
#開発タブを選択
position=pgui.locateOnScreen('jpgdeveloptab.jpg' , confidence=0.9)
pgui.click(position)
#マクロを選択
position=pgui.locateOnScreen('jpgmacro.jpg' , confidence=0.9)
pgui.click(position)
time.sleep(1)
#マクロを実行
position=pgui.locateOnScreen('jpgexe.jpg' , confidence=0.9)
pgui.click(position)