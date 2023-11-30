from typing import Callable
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
 
class DirectoryWatcher:
    def __init__(self, path: str, func: Callable[[FileSystemEvent], None]):
        """ 初期処理
            path(str) : 監視対象フォルダ
            func      : コールバック関数( func(event) )
        """
        # ファイル／フォルダ変化時のイベントハンドラ
        class EventHandler(FileSystemEventHandler):
            def __init__(self, func: Callable[[FileSystemEvent], None]):
                self.func = func
            def on_any_event(self, event: FileSystemEvent):      
                self.func(event)
        
        # Observerの生成と監視フォルダ、イベントハンドラの登録
        self.func = func
        self.observer = Observer()
        self.observer.schedule(EventHandler(self.func), path=path, recursive=True)

    def start(self) -> None:
        """ 監視の開始
        """
        self.observer.start()
 
    def stop(self) -> None:
        """ 監視の停止
        """
        self.observer.stop()