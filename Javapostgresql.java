
package javapostgresql;
import java.sql.;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Javapostgresql {
    private Connection c= null;
    private Statement  s = null;
    private ResultSet rs=null;
    
    
    
    public void cargarDriver(){
         System.out.println(Cargando driver.............); -------- Cargamos driver para poder despues establecer conexion y realizar consultas
        try{
            Class.forName(org.postgresql.Driver);
        } catch(ClassNotFoundException e){
            System.out.println(No hemos podido cargar driver n Salimos);
            e.printStackTrace();
            System.exit(1);
            }
        System.out.println(Driver cargado satisfactoriamente); ----- Hasta aqui cargamos driver.
    }
    
    public void connectDriver(String basededatos,String usuario,String contraseña){
        try {
            c=DriverManager.getConnection(jdbcpostgresqllocalhost+basededatos,pepe,contraseña);
        } catch (SQLException ex) {
            System.out.println(No se ha podido establecer conexión);
            ex.printStackTrace();
            System.exit(1);
        }
        if (c!=null) System.out.println(Conectado a la base de datos);
        else System.out.println(No se ha podido conectar a la base de datos);
    }
    public void Statement (){    
        try {
            s=c.createStatement();
        } catch (SQLException ex2) {
            System.out.println(Error en creación de statement);
            ex2.printStackTrace();
            System.exit(1);
        }
    }
    public void Execute (String execute){
          try {
            s.executeUpdate(Begin;n
                    +  + execute +  commit;); Ya que tenemos mayusculas en la relación tenemos que establecer este pequeño truco en el string para que detecte las comillas el execute.
        } catch (SQLException ex3) {
            System.out.println(No se ha podido ejecutar la query);
            ex3.printStackTrace();
            System.exit(1);
        }
    }
    public void Print(){
         int index = 0;
        try {
            while (rs.next()){
                System.out.println(Resultado de la fila + index +);
                System.out.println(rs.getString(1));
            }
        } catch (SQLException ex4) {
            System.out.println(Error al recoger datos);
            ex4.printStackTrace();
            System.exit(1);
        }
    }
    public void close(){
         try {
        s.close();
        c.close();
        } catch (SQLException ex5) {
             System.out.println(No se ha podido cerrar la conexion);
             ex5.printStackTrace();
             System.exit(1);
        }
    }
    public Javapostgresql(){
        
}
}