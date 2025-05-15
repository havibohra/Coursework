import vtk
import sys

def volume_render(input_file, use_phong):
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(input_file)
    reader.Update()
    
    volume_mapper = vtk.vtkSmartVolumeMapper()
    volume_mapper.SetInputConnection(reader.GetOutputPort())
    
    color_transfer = vtk.vtkColorTransferFunction()
    color_transfer.AddRGBPoint(-4931.54, 0, 1, 1)
    color_transfer.AddRGBPoint(-2508.95, 0, 0, 1)
    color_transfer.AddRGBPoint(-1873.9, 0, 0, 0.5)
    color_transfer.AddRGBPoint(-1027.16, 1, 0, 0)
    color_transfer.AddRGBPoint(-298.031, 1, 0.4, 0)
    color_transfer.AddRGBPoint(2594.97, 1, 1, 0)
    
    opacity_transfer = vtk.vtkPiecewiseFunction()
    opacity_transfer.AddPoint(-4931.54, 1.0)
    opacity_transfer.AddPoint(101.815, 0.002)
    opacity_transfer.AddPoint(2594.97, 0.0)
    
    volume_property = vtk.vtkVolumeProperty()
    volume_property.SetColor(color_transfer)
    volume_property.SetScalarOpacity(opacity_transfer)
    
    if use_phong:
        volume_property.ShadeOn()
        volume_property.SetAmbient(0.5)
        volume_property.SetDiffuse(0.5)
        volume_property.SetSpecular(0.5)
    
    volume = vtk.vtkVolume()
    volume.SetMapper(volume_mapper)
    volume.SetProperty(volume_property)
    
    outline = vtk.vtkOutlineFilter()
    outline.SetInputConnection(reader.GetOutputPort())
    outline_mapper = vtk.vtkPolyDataMapper()
    outline_mapper.SetInputConnection(outline.GetOutputPort())
    outline_actor = vtk.vtkActor()
    outline_actor.SetMapper(outline_mapper)
    
    renderer = vtk.vtkRenderer()
    renderer.AddVolume(volume)
    renderer.AddActor(outline_actor)
    
    render_window = vtk.vtkRenderWindow()
    render_window.SetSize(1000, 1000)
    render_window.AddRenderer(renderer)
    
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)
    
    render_window.Render()
    interactor.Start()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python volume_render.py <input.vti> <use_phong: 0 or 1>")
        sys.exit(1)
    
    input_vti = sys.argv[1]
    use_phong = bool(int(sys.argv[2]))
    volume_render(input_vti, use_phong)