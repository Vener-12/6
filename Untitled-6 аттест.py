/*
 * 1 Подумать над структурой класса смартфонов на склады техники - выделить поля и методы. Реализовать в java.
2 Создать множество смартфонов.
3 Написать метод, который будет запрашивать у пользователя критерий фильтрации и выведет смартфоны, отвечающие фильтру.
SmartPhone smartphone1 = new SmartPhone
SmartPhone smartphone2 = new SmartPhone 
SmartPhone smartphone3 = new SmartPhone 
SmartPhone smartphone4 = new SmartPhone 
SmartPhone smartphone5 = new SmartPhone 
Например: “Введите цифру, соответствующую необходимому критерию:
1 - ОЗУ
2 - Объем ЖД
3 - Операционная система
4 - Цвет
Далее нужно запросить минимальные значения для указанных критериев - сохранить параметры фильтрации можно также в Map.
Отфильтровать смартфоны их первоначального множества и вывести проходящие по условиям.
Класс сделать в отдельном файле
приветствие
Выбор параметра
выбор конкретнее
вывод подходящих
 */
public class laptop{
    private String color;
    private Integer RAM;
    private String OS;
    private Integer HDD;
    private Integer id;
    private String brand;
    private String model;
    private boolean isBooked = false;

    public laptop(String model,Integer id, String brand){
        this.model = model;
        this.brand = brand;
        this.id = id;
        System.out.println("Смартфон марки "+"'"+ this.brand+"'"+" Модель "+this.model+" С id " +Integer.toString(this.id));
    }
    public String getColor(){
        return this.color;
    }
    public Integer getRAM(){
        return this.RAM;
    }
    public String getOS(){
        return this.OS;
    }
    public Integer getHDD(){
        return this.HDD;
    }
    public Integer getid(){
        return this.id;
    }
    public String getBrand(){
        return this.brand;
    }
    public String getModel(){
        return this.model;
    }
    public Boolean getBooking(){
        return this.isBooked;
    }
    public void setColor(String color){
        this.color =color;
    }
    public void setRAM(Integer RAM){
        this.RAM = RAM;
    }
    public void setOS(String OS){
        this.OS = OS;
    }
    public void setHDD(Integer HDD){
        this.HDD = HDD;
    }
    public void Phone(){
        if (isBooked==false){
            this.isBooked=true;
        }
        else System.out.println("Этот смартфон уже зарезервирован");
    }
    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("Смартфон ");
        sb.append(this.id);
        sb.append(System.lineSeparator());
        sb.append(this.color);
        sb.append(" ");
        sb.append(this.brand);
        sb.append(" ");
        sb.append(this.model);
        sb.append(System.lineSeparator());
        sb.append("OS "+this.OS);
        sb.append(System.lineSeparator());
        sb.append("HDD "+this.HDD);
        sb.append(System.lineSeparator());
        sb.append("RAM "+this.RAM);
        sb.append(System.lineSeparator());
        if(this.isBooked==false) sb.append("Не зарезервирован");
        else sb.append("Зарезервирован");

        
        return(sb.toString());
    }

    

}
