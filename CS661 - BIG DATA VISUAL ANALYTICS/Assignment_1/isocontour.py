import vtk
import sys

def extract_isocontour(input_file, isovalue, output_file):
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(input_file)
    reader.Update()
    
    image_data = reader.GetOutput()
    dims = image_data.GetDimensions()
    
    contour_polydata = vtk.vtkPolyData()
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()
    
    point_id = 0
    
    for i in range(dims[0] - 1):
        for j in range(dims[1] - 1):
            cell_points = [(i, j), (i+1, j), (i+1, j+1), (i, j+1)]
            values = [image_data.GetScalarComponentAsDouble(x, y, 0, 0) for x, y in cell_points]
            
            edges = []
            for k in range(4):
                v1, v2 = values[k], values[(k+1) % 4]
                if (v1 < isovalue and v2 > isovalue) or (v1 > isovalue and v2 < isovalue):
                    ratio = (isovalue - v1) / (v2 - v1)
                    x1, y1 = cell_points[k]
                    x2, y2 = cell_points[(k+1) % 4]
                    x_interp = x1 + ratio * (x2 - x1)
                    y_interp = y1 + ratio * (y2 - y1)
                    pid = points.InsertNextPoint(x_interp, y_interp, 0)
                    edges.append(pid)
            
            if len(edges) == 2:
                line = vtk.vtkLine()
                line.GetPointIds().SetId(0, edges[0])
                line.GetPointIds().SetId(1, edges[1])
                lines.InsertNextCell(line)
    
    contour_polydata.SetPoints(points)
    contour_polydata.SetLines(lines)
    
    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName(output_file)
    writer.SetInputData(contour_polydata)
    writer.Write()
    print(f"Isocontour saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python isocontour.py <input.vti> <isovalue> <output.vtp>")
        sys.exit(1)
    
    input_vti = sys.argv[1]
    isovalue = float(sys.argv[2])
    output_vtp = sys.argv[3]
    extract_isocontour(input_vti, isovalue, output_vtp)
