function setoptions(brands, brands_id) {
  for (let i = 1; i <= brands.length; i++) {
          document.getElementById(i.toString()).innerHTML = brands[i-1];
          document.getElementById(i.toString()).value = brands_id[i-1];
        }
  if (brands.length != 10){
    for (let j = brands.length+1; j<=10; j++){
      document.getElementById(j).style.display = "none";
    }
  }
}



function hideselectionboxes(){
    document.getElementById("1").style.display= "none";
    document.getElementById("2").style.display= "none";
    document.getElementById("3").style.display= "none";
    document.getElementById("4").style.display= "none";
    document.getElementById("5").style.display= "none";
    document.getElementById("6").style.display= "none";
    document.getElementById("7").style.display= "none";
    document.getElementById("8").style.display= "none";
    document.getElementById("9").style.display= "none";
    document.getElementById("10").style.display= "none";
  }
/*
  function changed(){
    document.getElementById("userid").value = document.getElementById("selectbusiness").value;
  }
*/

  function showselectionboxes(){
    document.getElementById("1").style.display= "block";
    document.getElementById("2").style.display= "block";
    document.getElementById("3").style.display= "block";
    document.getElementById("4").style.display= "block";
    document.getElementById("5").style.display= "block";
    document.getElementById("6").style.display= "block";
    document.getElementById("7").style.display= "block";
    document.getElementById("8").style.display= "block";
    document.getElementById("9").style.display= "block";
    document.getElementById("10").style.display= "block";
  }

// hide selectionboxes
  hideselectionboxes();
  function showbusinesses(){
    // get value of selected category
    var category = document.getElementById("selectcategory").value;
    switch(category){
      case "clothing":
        showselectionboxes(); // show selection boxes
        const clothing_brands = [
          "J. Junaid Jamshed" , "Gul Ahmed" , "Nishat Linen", "Bareeze" , "Khaadi" , 
          "Kayseria", "KROSSKULTURE", "edenrobe", "OrientTextiles", "affordablepk"
        ];

        const clothing_brands_ids = [
          "@_JunaidJamshed" , "@GulahmedFashion" , "@nishatlinen","@BareezeOfficial" , 
          "@KhaadiOfficial" , "@KayseriaPK", "@KrossKulturePk" , "@edenrobe_pk" , 
          "@OrientTextiles", "@affordablepk"
        ];
        setoptions(clothing_brands, clothing_brands_ids);
        break;
        /*
        for (let i = 1; i <= clothing_brands.length; i++) {
          document.getElementById(i.toString()).innerHTML = clothing_brands[i-1];
          document.getElementById(i.toString()).value = clothing_brands_ids[i-1];
        }*/
        /*
        document.getElementById("1").innerHTML = "J. Junaid Jamshed";
        document.getElementById("1").value = "@_JunaidJamshed";
        document.getElementById("2").innerHTML = "Gul Ahmed";
        document.getElementById("2").value = "@GulahmedFashion";
        document.getElementById("3").innerHTML = "Nishat Linen";
        document.getElementById("3").value = "@nishatlinen";
        document.getElementById("4").innerHTML = "Bareeze";
        document.getElementById("4").value = "@BareezeOfficial";
        document.getElementById("5").innerHTML = "Khaadi";
        document.getElementById("5").value = "@KhaadiOfficial";
        document.getElementById("6").innerHTML = "Kayseria";
        document.getElementById("6").value = "@KayseriaPK";
        document.getElementById("7").innerHTML = "KROSSKULTURE";
        document.getElementById("7").value = "@KrossKulturePk"
        document.getElementById("8").innerHTML = "edenrobe";
        document.getElementById("8").value = "@edenrobe_pk";
        document.getElementById("9").innerHTML = "OrientTextiles";
        document.getElementById("9").value = "@OrientTextiles";
        document.getElementById("10").innerHTML = "affordablepk";
        document.getElementById("10").value = "@affordablepk";
        break;
        */

      case "foodonline":
        showselectionboxes(); // show selection boxes
        const food_brands = ["foodpanda" , "kfcpakistan" , "MENU", 
                                "Eat Mubarak" , "Supermeal Pakistan" , "K&N's Pakistan", "foodpakistan", 
                                "foodnerd", "cheetay"
                            ];

        const food_brands_ids = ["@foodpanda_pk" , "@kfc_pk" , "@Seasonsfoods",
                                    "@EatMubarak_Pk" , "@SupermealPK" , "@KandNs", 
                                    "@Foodpakistanpk" , "@Foodnerdpk" , "@cheetaypk"
                                ];
        setoptions(food_brands, food_brands_ids);
        break;
        /*
        for (let i = 1; i <= 9; i++) {
          document.getElementById(i.toString()).innerHTML = food_brands[i-1];
          document.getElementById(i.toString()).value = food_brands_ids[i-1];
        }
        */
        //document.getElementById("10").style.display = "none";
        /* 
        document.getElementById("1").innerHTML = "foodpanda";
        document.getElementById("1").value = "@foodpanda_pk";
        document.getElementById("2").innerHTML = "kfcpakistan";
        document.getElementById("2").value = "@kfc_pk";
        document.getElementById("3").innerHTML = "MENU";
        document.getElementById("3").value = "@Seasonsfoods";
        document.getElementById("4").innerHTML = "Eat Mubarak";
        document.getElementById("4").value = "@EatMubarak_Pk";
        document.getElementById("5").innerHTML = "Supermeal Pakistan";
        document.getElementById("5").value = "@SupermealPK";
        document.getElementById("6").innerHTML = "K&N's Pakistan";
        document.getElementById("6").value = "@KandNs";
        document.getElementById("7").innerHTML = "foodpakistan";
        document.getElementById("7").value = "@Foodpakistanpk";
        document.getElementById("8").innerHTML = "foodnerd";
        document.getElementById("8").value = "@Foodnerdpk";
        document.getElementById("9").innerHTML = "cheetay";
        document.getElementById("9").value = "@cheetaypk";
        document.getElementById("10").style.display = "none";
        document.getElementById("10").style.display = "none";
        */
        /*
        document.getElementById("9").innerHTML = "";
        document.getElementById("9").value = "";
        document.getElementById("10").innerHTML = "";
        document.getElementById("10").value = "";
        */

      case "onlineshopping":
        showselectionboxes();
        const shopping_brands = [
          "Amazon", "AliExpress" , "HomeShopping", "iShoppingpk" , "Daraz" , "Alibaba" ,
          "Elo" , "Telemart Official" , "Tejar.pk" , "Goto Online Shopping"
        ]; 

        const shopping_brands_id = [
          "@amazon" , "@AliExpress_EN" , "@homeshoppingpk" , "@iShoppingpk" , 
          "@darazpk" , "@AlibabaB2B", "@ExportLeftovers" , "@Telemartstores",
          "@TejarPK" , "@GotocomPk"
        ];
        setoptions(shopping_brands , shopping_brands);
        break;
        /*
        document.getElementById("1").innerHTML = "Amazon";
        document.getElementById("1").value = "@amazon";
        document.getElementById("2").innerHTML = "AliExpress";
        document.getElementById("2").value = "@AliExpress_EN";
        document.getElementById("3").innerHTML = "HomeShopping";
        document.getElementById("3").value = "@homeshoppingpk";
        document.getElementById("4").innerHTML = "iShoppingpk";
        document.getElementById("4").value = "@iShoppingpk";
        document.getElementById("5").innerHTML = "Daraz";
        document.getElementById("5").value = "@darazpk";
        document.getElementById("6").innerHTML = "Alibaba";
        document.getElementById("6").value = "@AlibabaB2B";
        document.getElementById("7").innerHTML = "Elo";
        document.getElementById("7").value = "@ExportLeftovers";
        document.getElementById("8").innerHTML = "Telemart Official";
        document.getElementById("8").value = "@Telemartstores";
        document.getElementById("9").innerHTML = "Tejar.pk";
        document.getElementById("9").value = "@TejarPK";
        document.getElementById("10").innerHTML = "Goto Online Shopping";
        document.getElementById("10").value = "@GotocomPk";
        break;
      */
      case "mobilepayment":
        showselectionboxes(); // show selection boxes
        const mobilepayment = [
          "JazzCash" ,  "EasyPaisa" , "Zong PayMax" , "UBL Omni" , "Keenu Wallet" , "SimSim" , 
          "UPaisa" 
        ];

        const mobilepayment_id = [
          "@JazzCash" , "@easypaisa" , "@Zongers" , "@UBLDigital" , "@KeenuPak" , "@FINCA_Pakistan" , 
          "@UpaisaOfficial"
        ];
        setoptions(mobilepayment, mobilepayment_id);
        break;
        /*
        document.getElementById("1").innerHTML = "JazzCash";
        document.getElementById("1").value = "@JazzCash";
        document.getElementById("2").innerHTML = "EasyPaisa";
        document.getElementById("2").value = "@easypaisa";
        document.getElementById("3").innerHTML = "Zong PayMax";
        document.getElementById("3").value = "@Zongers";
        document.getElementById("4").innerHTML = "UBL Omni";
        document.getElementById("4").value = "@UBLDigital";
        document.getElementById("5").innerHTML = "Keenu Wallet";
        document.getElementById("5").value = "@KeenuPak";
        document.getElementById("6").innerHTML = "SimSim";
        document.getElementById("6").value = "@FINCA_Pakistan";
        document.getElementById("7").innerHTML = "UPaisa";
        document.getElementById("7").value = "@UpaisaOfficial";
        document.getElementById("8").style.display = "none";
        document.getElementById("9").style.display = "none";
        document.getElementById("10").style.display = "none";
        */
        /*
        document.getElementById("8").innerHTML = "";
        document.getElementById("8").value = "";
        document.getElementById("9").innerHTML = "";
        document.getElementById("9").value = "";
        document.getElementById("10").innerHTML = "";
        document.getElementById("10").value = "";
        */
        //break;
        
      case "footwear":
        showselectionboxes();
        const footwear = [
          "Stylo Shoes" , "Unze London (Pakistan)" , "Hush Puppies PK" , "Cat Footwear" , "Borjan Shoes" ,
          "Metro Shoes Pakistan" , "Bata Pakistan" , "Starlet Shoes"
        ];
        const footwear_id = [
          "@StyloShoesPK" , "@unzepakistan" , "@HushPuppiesPak" , "@CatFootwear" , "@borjanshoes1" ,
          "@MetroShoesbyNY" , "@BataHomePK" , "@onlinestarlet"
        ] ;
        setoptions(footwear, footwear_id);
        break;
        /*
        document.getElementById("1").innerHTML = "Stylo Shoes";
        document.getElementById("1").value = "@StyloShoesPK";
        document.getElementById("2").innerHTML = "Unze London (Pakistan)";
        document.getElementById("2").value = "@unzepakistan";
        document.getElementById("3").innerHTML = "Hush Puppies PK";
        document.getElementById("3").value = "@HushPuppiesPak";
        document.getElementById("4").innerHTML = "Cat Footwear";
        document.getElementById("4").value = "@CatFootwear";
        document.getElementById("5").innerHTML = "Borjan Shoes";
        document.getElementById("5").value = "@borjanshoes1";
        document.getElementById("6").innerHTML = "Metro Shoes Pakistan";
        document.getElementById("6").value = "@MetroShoesbyNY";
        document.getElementById("7").innerHTML = "Bata Pakistan";
        document.getElementById("7").value = "@BataHomePK";
        document.getElementById("8").innerHTML = "Starlet Shoes";
        document.getElementById("8").value = "@onlinestarlet";
        document.getElementById("9").style.display = "none";
        document.getElementById("10").style.display = "none";
        */
        /*
        document.getElementById("9").innerHTML = "";
        document.getElementById("9").value = "";
        document.getElementById("10").innerHTML = "";
        document.getElementById("10").value = "";
        */
        //break;

      case "property":
        showselectionboxes(); // show selection boxes
        const property = [
          "Bahria Town Official", "DHA", "Abdullah Group", "Habib Rafiq", "Ali Builders & Developers",
          "ZEM Builders", "Lahore Development Authority (LDA)."
        ]; 

        const property_id = [
          "@BahriaTownOffic", "@DHAToday", "@ABDBuilders", "@habibrafiqpvt", "@alibuilders", "@zembuilders", 
          "@LHRDevAuthority"
        ];
        setoptions(property, property_id);
        break;
        /*
        document.getElementById("1").innerHTML = "Bahria Town Official";
        document.getElementById("1").value = "@BahriaTownOffic";
        document.getElementById("2").innerHTML = "DHA";
        document.getElementById("2").value = "@DHAToday";
        document.getElementById("3").innerHTML = "Abdullah Group";
        document.getElementById("3").value = "@ABDBuilders";
        document.getElementById("4").innerHTML = "Habib Rafiq";
        document.getElementById("4").value = "@habibrafiqpvt";
        document.getElementById("5").innerHTML = "Ali Builders & Developers";
        document.getElementById("5").value = "@alibuilders";
        document.getElementById("6").innerHTML = "ZEM Builders";
        document.getElementById("6").value = "@zembuilders";
        document.getElementById("7").innerHTML = "Lahore Development Authority (LDA).";
        document.getElementById("7").value = "@LHRDevAuthority";
        document.getElementById("8").style.display = "none";
        document.getElementById("9").style.display = "none";
        document.getElementById("10").style.display = "none";
        */
        /*
        document.getElementById("7").value = ""
        document.getElementById("8").innerHTML = "";
        document.getElementById("8").value = "";
        document.getElementById("9").innerHTML = "";
        document.getElementById("9").value = "";
        document.getElementById("10").innerHTML = "";
        document.getElementById("10").value = "";
        */
        //break;

      case "beverage":
        showselectionboxes(); // show selection boxes
        const beverage = [
          "Pakola Pakistan", "pepsipakistan", "Coca-Cola Pakistan", "Murree Brewery", "NESTLÉ PURE LIFE",
          "Mountain Dew", "Sprite", "Fanta", "7UP Pakistan", "Mirinda Pakistan"
        ];

        const beverage_id = [
          "@PakolaPakistan", "@pepsipakistan", "@CokePk", "@MurreeBrewery", "@PureLifePK", "@DewPK",
           "@Sprite", "@fantapakistan", "@7UP_PK", "@MirindaPK"
        ];
        setoptions(beverage, beverage_id);
        break;
        /*
        document.getElementById("1").innerHTML = "Pakola Pakistan";
        document.getElementById("1").value = "@PakolaPakistan";
        document.getElementById("2").innerHTML = "pepsipakistan";
        document.getElementById("2").value = "@pepsipakistan";
        document.getElementById("3").innerHTML = "Coca-Cola Pakistan";
        document.getElementById("3").value = "@CokePk";
        document.getElementById("4").innerHTML = "Murree Brewery";
        document.getElementById("4").value = "@MurreeBrewery";
        document.getElementById("5").innerHTML = "NESTLÉ PURE LIFE";
        document.getElementById("5").value = "@PureLifePK";
        document.getElementById("6").innerHTML = "Mountain Dew";
        document.getElementById("6").value = "@DewPK";
        document.getElementById("7").innerHTML = "Sprite";
        document.getElementById("7").value = "@Sprite";
        document.getElementById("8").innerHTML = "Fanta";
        document.getElementById("8").value = "@fantapakistan";
        document.getElementById("9").innerHTML = "7UP Pakistan";
        document.getElementById("9").value = "@7UP_PK";
        document.getElementById("10").innerHTML = "Mirinda Pakistan";
        document.getElementById("10").value = "@MirindaPK";
        break;*/
      case "banks":
        showselectionboxes(); // show selection boxes
        const banks = [
          "SBP", "National Bank Of Pakistan NBP", "Sindh Bank Ltd", "Bank Of Khyber", 
          "First Women Bank Limited", "Askari Bank Limited", "Bank Alfalah", "MCB Bank Limited", 
          "The Bank of Punjab"
        ];
        const banks_id = [
          "@StateBank_Pak", "@nationalbankpk", "@SINDHBANKMEDIA", "@TheBankofKhyber", "@FWBLbank", 
          "@Askari_Bank", "@BankAlfalahPAK", "@MCBBankPk", "@thebankofpunjab"
        ];
        setoptions(banks, banks_id);
        break;
        /*
        document.getElementById("1").innerHTML = "SBP";
        document.getElementById("1").value = "@StateBank_Pak";
        document.getElementById("2").innerHTML = "National Bank Of Pakistan NBP";
        document.getElementById("2").value = "@nationalbankpk";
        document.getElementById("3").innerHTML = "Sindh Bank Ltd";
        document.getElementById("3").value = "@SINDHBANKMEDIA";
        document.getElementById("4").innerHTML = "Bank Of Khyber";
        document.getElementById("4").value = "@TheBankofKhyber";
        document.getElementById("5").innerHTML = "First Women Bank Limited";
        document.getElementById("5").value = "@FWBLbank";
        document.getElementById("6").innerHTML = "Askari Bank Limited";
        document.getElementById("6").value = "@Askari_Bank";
        document.getElementById("7").innerHTML = "Bank Alfalah";
        document.getElementById("7").value = "@BankAlfalahPAK";
        document.getElementById("8").innerHTML = "Bank AL Habib Limited";
        document.getElementById("8").value = "@BAHLOfficial";
        document.getElementById("9").innerHTML = "MCB Bank Limited";
        document.getElementById("9").value = "@MCBBankPk";
        document.getElementById("10").innerHTML = "The Bank of Punjab";
        document.getElementById("10").value = "@thebankofpunjab";
        break;*/
      case "mobileoperator":
        showselectionboxes(); // show selection boxes
        const mobileoperator = [
          "Telenor, Pakistan", "Jazz", "ufone", "Zong", "Warid Telecom" 
        ];
        const mobileoperator_id = [
          "@telenorpakistan", "@jazzpk", "@Ufone", "@Zongers", "@Waridpak"
        ];
        setoptions(mobileoperator, mobileoperator_id);
        break;
        /*
        document.getElementById("1").innerHTML = "Telenor Pakistan";
        document.getElementById("1").value = "@telenorpakistan";
        document.getElementById("2").innerHTML = "Jazz";
        document.getElementById("2").value = "@jazzpk";
        document.getElementById("3").innerHTML = "ufone";
        document.getElementById("3").value = "@Ufone";
        document.getElementById("4").innerHTML = "Zong";
        document.getElementById("4").value = "@Zongers";
        document.getElementById("5").innerHTML = "Warid Telecom";
        document.getElementById("5").value = "@Waridpak";
        document.getElementById("6").style.display = "none";
        document.getElementById("7").style.display = "none";
        document.getElementById("8").style.display = "none";
        document.getElementById("9").style.display = "none";
        document.getElementById("10").style.display = "none";
        break;
        */
      case "automobiles":
        showselectionboxes(); // show selection boxes
        const automobiles = [
          "Toyota Pakistan", "Suzuki Pakistan", "Yamaha Motor Pakistan", "MG Motor Pakistan",
          "Honda Atlas Cars Pakistan Limited", "Kia Motors Pakistan", "Audi Pakistan", "JAGUAR PAKISTAN LTD.",
          "Lamborghini", "Mercedes-Benz"
        ];

        const automobiles_id = [
          "@ToyotaPak", "@SuzukiPakistan", "@YamahaMotorPk", "@MGPakistan", "@HACPLOfficial", "@KiaMotorsPK",
          "@AudiPakistan", "@Jaguarpakistan", "@Lamborghini", "@MercedesBenz"

        ];
        setoptions(automobiles, automobiles_id);
        break;
      
      case "technology":
        showselectionboxes(); // show selection boxes
        const technology = [
          "Microsoft", "Amazon Inc", "Alphabet Inc", "Tencent", "Facebook", "Alibaba Group", "Nvidia", "TSMC"
        ];
        const technology_id = [ 
          "@Microsoft", "@amazon", "@Alphabetlnc", "@TencentGlobal", "@Facebook", "@AlibabaGroup", "@nvidia",
          "@TSMCGlobal" 
        ];
        setoptions(technology, technology_id);
        break;
        /*
        document.getElementById("1").innerHTML = "Microsoft";
        document.getElementById("1").value = "@Microsoft";
        document.getElementById("2").innerHTML = "Amazon Inc";
        document.getElementById("2").value = "@amazon";
        document.getElementById("3").innerHTML = "Alphabet Inc";
        document.getElementById("3").value = "@Alphabetlnc";
        document.getElementById("4").innerHTML = "Tencent";
        document.getElementById("4").value = "@TencentGlobal";
        document.getElementById("5").innerHTML = "Facebook";
        document.getElementById("5").value = "@Facebook";
        document.getElementById("6").innerHTML = "Alibaba Group";
        document.getElementById("6").value = "@AlibabaGroup";
        document.getElementById("7").innerHTML = "Nvidia";
        document.getElementById("7").value = "@nvidia";
        document.getElementById("8").innerHTML = "TSMC";
        document.getElementById("8").value = "@TSMCGlobal";
        document.getElementById("9").innerHTML = "Samsung";
        document.getElementById("9").value = "";
        document.getElementById("10").innerHTML = "";
        document.getElementById("10").value = "";
        break;
        */
      /*case "smartphones":
        showselectionboxes(); // show selection boxes
        document.getElementById("1").innerHTML = "";
        document.getElementById("1").value = "";
        document.getElementById("2").innerHTML = "";
        document.getElementById("2").value = "";
        document.getElementById("3").innerHTML = "";
        document.getElementById("3").value = "";
        document.getElementById("4").innerHTML = "";
        document.getElementById("4").value = "";
        document.getElementById("5").innerHTML = "";
        document.getElementById("5").value = "";
        document.getElementById("6").value = "";
        document.getElementById("7").innerHTML = "";
        document.getElementById("7").value = "";
        document.getElementById("8").innerHTML = "";
        document.getElementById("8").value = "";
        document.getElementById("9").innerHTML = "";
        document.getElementById("9").value = "";
        document.getElementById("10").innerHTML = "";
        document.getElementById("10").value = "";
        break;
      */
        default:
        hideselectionboxes(); // call function for hiding selection boxes
  }}
/*
if(document.getElementById("selectcategory").value!='Select Business Category' & document.getElementById('nooftweets').value !='Select No of Tweets'){

  document.getElementById("selectbusiness").value = '{{option_value}}';
}
*/