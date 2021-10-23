
            var units;
            var amount,sur_charge,total_amount;

            units=prompt("Enter the UNITS your consumed: ");
            if(units<50){
                amount=units*2.60;
                sur_charge=25;
            }
            else if(units<=100){
                amount=130+((units-50)*3.25);
                sur_charge=35;
            }
            else if(units<=200){
                amount=130+162.50+((units-100)*5.26);
                sur_charge=45;
            
            }
            else
            {
                amount=130+162.50+526+((units-200)*7.75);
                sur_charge=55;
            }
            total_amount=amount+sur_charge;
            document.getElementById("h1id").innerHTML=("Electricity Bill = "+total_amount+" /-");
