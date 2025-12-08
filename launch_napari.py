from napari import Viewer, run

viewer = Viewer()
dock_widget, plugin_widget = viewer.window.add_plugin_dock_widget(
    "nagini3d-napari", "Nagini3D Segmentation tool"
)
run()
