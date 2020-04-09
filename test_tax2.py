import mock
from tax2 import tax_calculation

@mock.patch('builtins.input', side_effect=['2', '400000', '370000'])
def test_1(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 18000
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 220000
   assert val['individual_tax'] == 43900
   assert val['standard_tax'] == 110100
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 61900

@mock.patch('builtins.input', side_effect=['2', '400000', '320000'])
def test_2(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 16000
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 172000
   assert val['individual_tax'] == 36580
   assert val['standard_tax'] == 102900
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 53740

@mock.patch('builtins.input', side_effect=['2', '400000', '270000'])
def test_3(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 13500
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 124500
   assert val['individual_tax'] == 30950
   assert val['standard_tax'] == 95775
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 45665

@mock.patch('builtins.input', side_effect=['2', '400000', '220000'])
def test_4(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 11000
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 77000
   assert val['individual_tax'] == 27120
   assert val['standard_tax'] == 88650
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 37590

@mock.patch('builtins.input', side_effect=['2', '400000', '180000'])
def test_5(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 9000
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 39000
   assert val['individual_tax'] == 25280
   assert val['standard_tax'] == 82950
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 31130

@mock.patch('builtins.input', side_effect=['2', '400000', '140000'])
def test_6(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 7000
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 1000
   assert val['individual_tax'] == 24520
   assert val['standard_tax'] == 77250
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 24670

@mock.patch('builtins.input', side_effect=['2', '400000', '90000'])
def test_7(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 4500
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 24500
   assert val['standard_tax'] == 70125
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 16595

@mock.patch('builtins.input', side_effect=['2', '400000', '30000'])
def test_8(self):
   val = tax_calculation()
   assert val['mpf'][0] == 18000
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 250000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 24500
   assert val['standard_tax'] == 61800
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 8800

@mock.patch('builtins.input', side_effect=['2', '350000', '320000'])
def test_9(self):
   val = tax_calculation()
   assert val['mpf'][0] == 17500
   assert val['mpf'][1] == 16000
   assert val['nci'][0] == 200500
   assert val['nci'][1] == 172000
   assert val['individual_tax'] == 28165
   assert val['standard_tax'] == 95475
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 45325

@mock.patch('builtins.input', side_effect=['2', '350000', '270000'])
def test_10(self):
   val = tax_calculation()
   assert val['mpf'][0] == 17500
   assert val['mpf'][1] == 13500
   assert val['nci'][0] == 200500
   assert val['nci'][1] == 124500
   assert val['individual_tax'] == 22535
   assert val['standard_tax'] == 88350
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 37250

@mock.patch('builtins.input', side_effect=['2', '350000', '220000'])
def test_11(self):
   val = tax_calculation()
   assert val['mpf'][0] == 17500
   assert val['mpf'][1] == 11000
   assert val['nci'][0] == 200500
   assert val['nci'][1] == 77000
   assert val['individual_tax'] == 18705
   assert val['standard_tax'] == 81225
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 29175

@mock.patch('builtins.input', side_effect=['2', '350000', '180000'])
def test_12(self):
   val = tax_calculation()
   assert val['mpf'][0] == 17500
   assert val['mpf'][1] == 9000
   assert val['nci'][0] == 200500
   assert val['nci'][1] == 39000
   assert val['individual_tax'] == 16865
   assert val['standard_tax'] == 75525
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 22715

@mock.patch('builtins.input', side_effect=['2', '350000', '140000'])
def test_13(self):
   val = tax_calculation()
   assert val['mpf'][0] == 17500
   assert val['mpf'][1] == 7000
   assert val['nci'][0] == 200500
   assert val['nci'][1] == 1000
   assert val['individual_tax'] == 16105
   assert val['standard_tax'] == 69825
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 16255

@mock.patch('builtins.input', side_effect=['2', '350000', '90000'])
def test_14(self):
   val = tax_calculation()
   assert val['mpf'][0] == 17500
   assert val['mpf'][1] == 4500
   assert val['nci'][0] == 200500
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 16085
   assert val['standard_tax'] == 62700
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 9560

@mock.patch('builtins.input', side_effect=['2', '350000', '30000'])
def test_15(self):
   val = tax_calculation()
   assert val['mpf'][0] == 17500
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 200500
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 16085
   assert val['standard_tax'] == 54375
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 3910

@mock.patch('builtins.input', side_effect=['2', '300000', '270000'])
def test_16(self):
   val = tax_calculation()
   assert val['mpf'][0] == 15000
   assert val['mpf'][1] == 13500
   assert val['nci'][0] == 153000
   assert val['nci'][1] == 124500
   assert val['individual_tax'] == 15870
   assert val['standard_tax'] == 81225
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 29175

@mock.patch('builtins.input', side_effect=['2', '300000', '220000'])
def test_17(self):
   val = tax_calculation()
   assert val['mpf'][0] == 15000
   assert val['mpf'][1] == 11000
   assert val['nci'][0] == 153000
   assert val['nci'][1] == 77000
   assert val['individual_tax'] == 12040
   assert val['standard_tax'] == 74100
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 21100

@mock.patch('builtins.input', side_effect=['2', '300000', '180000'])
def test_18(self):
   val = tax_calculation()
   assert val['mpf'][0] == 15000
   assert val['mpf'][1] == 9000
   assert val['nci'][0] == 153000
   assert val['nci'][1] == 39000
   assert val['individual_tax'] == 10200
   assert val['standard_tax'] == 68400
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 14880

@mock.patch('builtins.input', side_effect=['2', '300000', '140000'])
def test_19(self):
   val = tax_calculation()
   assert val['mpf'][0] == 15000
   assert val['mpf'][1] == 7000
   assert val['nci'][0] == 153000
   assert val['nci'][1] == 1000
   assert val['individual_tax'] == 9440
   assert val['standard_tax'] == 62700
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 9560

@mock.patch('builtins.input', side_effect=['2', '300000', '90000'])
def test_20(self):
   val = tax_calculation()
   assert val['mpf'][0] == 15000
   assert val['mpf'][1] == 4500
   assert val['nci'][0] == 153000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 9420
   assert val['standard_tax'] == 55575
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 4650

@mock.patch('builtins.input', side_effect=['2', '300000', '30000'])
def test_21(self):
   val = tax_calculation()
   assert val['mpf'][0] == 15000
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 153000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 9420
   assert val['standard_tax'] == 47250
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 1060

@mock.patch('builtins.input', side_effect=['2', '250000', '220000'])
def test_22(self):
   val = tax_calculation()
   assert val['mpf'][0] == 12500
   assert val['mpf'][1] == 11000
   assert val['nci'][0] == 105500
   assert val['nci'][1] == 77000
   assert val['individual_tax'] == 7170
   assert val['standard_tax'] == 66975
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 13550

@mock.patch('builtins.input', side_effect=['2', '250000', '180000'])
def test_23(self):
   val = tax_calculation()
   assert val['mpf'][0] == 12500
   assert val['mpf'][1] == 9000
   assert val['nci'][0] == 105500
   assert val['nci'][1] == 39000
   assert val['individual_tax'] == 5330
   assert val['standard_tax'] == 61275
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 8450

@mock.patch('builtins.input', side_effect=['2', '250000', '140000'])
def test_24(self):
   val = tax_calculation()
   assert val['mpf'][0] == 12500
   assert val['mpf'][1] == 7000
   assert val['nci'][0] == 105500
   assert val['nci'][1] == 1000
   assert val['individual_tax'] == 4570
   assert val['standard_tax'] == 55575
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 4650

@mock.patch('builtins.input', side_effect=['2', '250000', '90000'])
def test_25(self):
   val = tax_calculation()
   assert val['mpf'][0] == 12500
   assert val['mpf'][1] == 4500
   assert val['nci'][0] == 105500
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 4550
   assert val['standard_tax'] == 48450
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 1540

@mock.patch('builtins.input', side_effect=['2', '250000', '30000'])
def test_26(self):
   val = tax_calculation()
   assert val['mpf'][0] == 12500
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 105500
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 4550
   assert val['standard_tax'] == 40125
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 70

@mock.patch('builtins.input', side_effect=['2', '200000', '180000'])
def test_27(self):
   val = tax_calculation()
   assert val['mpf'][0] == 10000
   assert val['mpf'][1] == 9000
   assert val['nci'][0] == 58000
   assert val['nci'][1] == 39000
   assert val['individual_tax'] == 2260
   assert val['standard_tax'] == 54150
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 3820

@mock.patch('builtins.input', side_effect=['2', '200000', '140000'])
def test_28(self):
   val = tax_calculation()
   assert val['mpf'][0] == 10000
   assert val['mpf'][1] == 7000
   assert val['nci'][0] == 58000
   assert val['nci'][1] == 1000
   assert val['individual_tax'] == 1500
   assert val['standard_tax'] == 48450
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 1540

@mock.patch('builtins.input', side_effect=['2', '200000', '90000'])
def test_29(self):
   val = tax_calculation()
   assert val['mpf'][0] == 10000
   assert val['mpf'][1] == 4500
   assert val['nci'][0] == 58000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 1480
   assert val['standard_tax'] == 41325
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 230

@mock.patch('builtins.input', side_effect=['2', '200000', '30000'])
def test_30(self):
   val = tax_calculation()
   assert val['mpf'][0] == 10000
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 58000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 1480
   assert val['standard_tax'] == 33000
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 0

@mock.patch('builtins.input', side_effect=['2', '160000', '140000'])
def test_31(self):
   val = tax_calculation()
   assert val['mpf'][0] == 8000
   assert val['mpf'][1] == 7000
   assert val['nci'][0] == 20000
   assert val['nci'][1] == 1000
   assert val['individual_tax'] == 420
   assert val['standard_tax'] == 42750
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 420

@mock.patch('builtins.input', side_effect=['2', '160000', '90000'])
def test_32(self):
   val = tax_calculation()
   assert val['mpf'][0] == 8000
   assert val['mpf'][1] == 4500
   assert val['nci'][0] == 20000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 400
   assert val['standard_tax'] == 35625
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 0

@mock.patch('builtins.input', side_effect=['2', '160000', '30000'])
def test_33(self):
   val = tax_calculation()
   assert val['mpf'][0] == 8000
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 20000
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 400
   assert val['standard_tax'] == 27300
   assert val['recommend'] == 'joint'
   assert val['joint_tax'] == 0

@mock.patch('builtins.input', side_effect=['2', '120000', '90000'])
def test_34(self):
   val = tax_calculation()
   assert val['mpf'][0] == 6000
   assert val['mpf'][1] == 4500
   assert val['nci'][0] == 0
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 0
   assert val['standard_tax'] == 29925
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 0

@mock.patch('builtins.input', side_effect=['2', '120000', '30000'])
def test_35(self):
   val = tax_calculation()
   assert val['mpf'][0] == 6000
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 0
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 0
   assert val['standard_tax'] == 21600
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 0

@mock.patch('builtins.input', side_effect=['2', '50000', '30000'])
def test_36(self):
   val = tax_calculation()
   assert val['mpf'][0] == 0
   assert val['mpf'][1] == 0
   assert val['nci'][0] == 0
   assert val['nci'][1] == 0
   assert val['individual_tax'] == 0
   assert val['standard_tax'] == 12000
   assert val['recommend'] == 'seperate'
   assert val['joint_tax'] == 0