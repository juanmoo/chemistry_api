# API for polymer reaction synthesis extractor
API Deployement of reaction synthesis extraction model.

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Starting API
This project uses Flask to implement its API and can be start using the follwing command:
```bash
python main.py
```

### Creating extractions
In order to analyse the contents of a paragarph that describes a polymer synthesis reaction, the paragraphs should be passed in a JSON object to the "/extract" endpoint of the API. For example, if the server were to be running locally in port 5000 the follwing would result in the server respoinding with the extraction to the three embedded paragraphs:

```bash
curl -X POST http://localhost:5000/extract \
-H "Content-Type: application/json" \
-d '{
        "paragraphs": [
            "Under an inert atmosphere the Mg(BHT)2(THF)2 catalyst 1 was dissolved in anhydrous degassed toluene ( 425 mL ) and anhydrous degassed propylene oxide ( 105 mL , 1.50 mol ) was added . Anhydrous , degassed propargyl alcohol initiator ( 8.66 mL , 0.15 mol ) was added , followed by the addition of powdered maleic anhydride ( 147.0 g , 1.50 mol ) . The reaction was heated to 80 \u00b0 C to begin the polymerization , and aliquots were removed to check conversion of the maleic anhydride . Upon full conversion ( ca . 45 h ) , the polymerization was cooled and quenched by the addition of 3 mL of CHCl3 . The polymer was precipitated into cold hexanes and dried to afford a yellow - orange viscous liquid . 1H NMR : ( 500 MHz , CDCl3 ) , \u03b4 ( ppm ) : 6.34 - 6.24 ( m , 20H , OC(=O)-CH = CH - C(=O)O ) , 5.32 - 5.22 ( s , br , 10H CH2-CH(CH3)-O ) , 4.78 ( s , HC\u2261C - CH2-O ) , 4.35 - 4.24 ( m , 20H , CH2CH(CH3)O ) , 2.54 ( s , 1H , HC\u2261C - CH2-O ) , 1.35 - 1.32 ( d , 30H , CH3 ) . 13C NMR : ( 125 MHz , CDCl3 ) , \u03b4 ( PPM ) : 166.7 ( C = O ) , 131.6 ( OC(=O)-CH = CH - C(=O)O ) , 75.8 ( HC C - CH2 ) , 70.1 ( CH2CH(CH3)O ) , 69.1 ( CH2CH(CH3)O ) , 51.1 ( HC C - CH2 ) , 16.2 ( CH3 ) .",
            "In an Etelux glovebox , the appropriate amount of carboxylate ( 0.01 mmol , 1 equiv . ) , cyclic anhydride ( 0.1 mmol , 100 equiv . ) were added in an oven - dried tube equipped with a magnetic stir , followed by epoxide ( 0.5 mmol , 500 equiv . ) . The tube was removed from the glovebox and placed in an aluminum heating block ( 110 oC ) for 1.5 h. The reaction mixture was diluted with approximately 10 mL dichloromethane and dropwise precipitated into 100 mL of methanol by hydrochloric acid with vigorous stirring , then the methanol were filtrated or poured out . The resulting polymers were dried under vacuum at 40 \u00baC.",
            "The palladium catalyst ( 1.27 \u00d7 10\u22125 mol ) and 1,4-benzoquinone ( [ BQ]/[Pd ] = 5 ) were dissolved in dichloromethane and then added to the flask . After the establishment of the reaction temperature ( 15 \u00b0 C ) , the system was continuously stirred for 5 min and then vinyl arene comonomer ( [ vinyl arene]/[Pd ] = 6800 ) was injected by a syringe into the well - stirred solution . The reaction temperature of 15 \u00b0 C was controlled with a cooler in polymerization experiments . The polymerization proceeded for 24 h at 1 atm CO ( absolute pressure ) . The resulting polymer was precipitated with acidic methanol ( 95:5 methanol / HCl ) and washed with methanol . To remove metallic palladium , the polymer was dissolved in chloroform , filtered through Celite , and precipitated with methanol . The solid was washed thoroughly with methanol and dried under vacuum to a constant weight ."
        ]
    }'
```