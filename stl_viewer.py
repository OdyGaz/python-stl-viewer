import pyvista as pv

# Ορίστε τη διαδρομή του αρχείου STL
file_path = "Spiral_worldcup.stl" 

try:
    # Φόρτωση του STL αρχείου
    mesh = pv.read(file_path)

    # Δημιουργία παραθύρου και εμφάνιση του 3D μοντέλου
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color="lightblue")
    plotter.show_grid()
    plotter.show()
except Exception as e:
    print(f"Παρουσιάστηκε σφάλμα κατά τη φόρτωση του αρχείου: {e}")