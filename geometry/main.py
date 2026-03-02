from random import randint as rand
import geometry.area, geometry.perimeter


def main():
    r = rand(1, 10)  
    latura_patrat = rand(1, 10) 
    lungime_drept = rand(1, 10) 
    latime_drept = rand(1, 10) 

    print(f"Valorile generate sunt: raza={r}, latura_patrat={latura_patrat}, Lungime_dreptunghi={lungime_drept}, latime_dreptunghi={latime_drept}")

    print(f"Arie Cerc: {area.cerc(r)}")
    print(f"Arie Patrat: {area.patrat(latura_patrat)}")
    print(f"Arie Dreptunghi: {area.dreptunghi(lungime_drept, latime_drept)}")

    print(f"Perimetru Cerc: {perimeter.cerc(r)}")
    print(f"Perimetru Patrat: {perimeter.patrat(latura_patrat)}")
    print(f"Perimetru Dreptunghi: {perimeter.dreptunghi(lungime_drept, latime_drept)}")


if __name__ == "__main__":
    main()