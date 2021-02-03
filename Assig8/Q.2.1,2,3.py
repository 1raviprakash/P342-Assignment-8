import matplotlib.pyplot as plt
import My_lib as M_L


V = []
error = []
Step = []
Analytical_Val = 12.56637


def fun(x, y, z):
    return ((x**2)/(1**2))+((y**2)/(1.5**2))+((z**2)/(2**2))


print("{:<15}{:<20}".format("Step", "Volume of ellipsoid"))
N = 50000
i = 0
while i < N:
    i = i+100
    Fn, X1, Y1, Z1, frac_err = M_L.Monte_Carlo_Vol(
        -1, 1, -1.5, 1.5, -2, 2, fun, i, Analytical_Val)

    Step.append(i)
    V.append(Fn)
    error.append(frac_err)
    print("{:<15}{:<20}".format(i, Fn))

sum_ans = 0
sum_err = 0
for i in range(len(V)):
    sum_ans = sum_ans + V[i]
    sum_err = sum_err + error[i]
print("\nVolume = ", sum_ans/len(V))
print("\nFractional Error =", sum_err/len(error))


plt.figure()
plt.plot(Step, V)
plt.axhline(12.56637, color='r')

plt.text(30000, 12.6, "Analytical value = 12.56637", size=16,
         va="baseline", ha="left", multialignment="left")
plt.title("Plot for Step vs Volume of ellipsoid")
plt.xlabel("Step")
plt.ylabel("Volume of ellipsoid")

plt.figure()
plt.plot(Step, error)

plt.title("Plot for Step vs Fractional error")
plt.xlabel("Step")
plt.ylabel("Fractional Error")
plt.show()


'''
Output


Step          Volume of ellipsoid 
100            12.959999999999999  
200            14.16               
300            13.200000000000001  
400            11.639999999999999  
500            11.856              
600            12.72               



700            12.377142857142857  
800            11.94               
900            12.853333333333333  
1000           12.48               
1100           12.72               
1200           12.52               
1300           12.461538461538463  
1400           12.754285714285714  
1500           12.784              
1600           12.705              
1700           12.32470588235294   
1800           12.213333333333335  
1900           12.492631578947368  
2000           12.6                
2100           12.845714285714285  
2200           13.298181818181819  
2300           12.104347826086958  
2400           12.280000000000001  
2500           12.815999999999999  
2600           12.673846153846155  
2700           12.462222222222222  
2800           12.54857142857143   
2900           12.107586206896553  
3000           12.24               
3100           12.95225806451613   
3200           12.15               
3300           12.64               
3400           12.847058823529412  
3500           12.479999999999999  
3600           12.48               
3700           12.389189189189189  
3800           12.719999999999999  
3900           12.76923076923077   
4000           12.775000000000001  
4100           12.526829268292683  
4200           12.84               
4300           12.44093023255814   
4400           12.360000000000001  
4500           12.842666666666666  
4600           12.365217391304348  
4700           12.55659574468085   
4800           12.745000000000001  
4900           12.504489795918367  
5000           12.2016             
5100           12.68705882352941   
5200           12.73846153846154   
5300           12.729056603773586  
5400           12.426666666666666  
5500           12.597818181818182  
5600           12.51               
5700           12.463157894736842  
5800           12.405517241379311  
5900           12.80135593220339   
6000           12.616              
6100           12.539016393442623  
6200           12.789677419354838  
6300           12.476190476190476  
6400           12.5025             
6500           12.716307692307693  
6600           12.421818181818182  
6700           12.497910447761194  
6800           12.578823529411766  
6900           12.699130434782608  
7000           12.517714285714286  
7100           12.83492957746479   
7200           12.760000000000002  
7300           12.575342465753426  
7400           12.502702702702702  
7500           12.6912             
7600           12.678947368421053  
7700           12.635844155844156  
7800           12.698461538461538  
7900           12.87493670886076   
8000           12.6                
8100           12.613333333333333  
8200           12.553170731707317  
8300           12.500240963855422  
8400           12.385714285714286  
8500           12.83294117647059   
8600           12.510697674418605  
8700           12.515862068965516  
8800           12.728181818181818  
8900           12.353258426966292  
9000           12.445333333333332  
9100           12.66989010989011   
9200           12.521739130434783  
9300           12.56516129032258   
9400           12.6                
9500           12.538105263157895  
9600           12.525              
9700           12.613608247422679  
9800           12.695510204081632  
9900           12.65939393939394   
10000          12.609599999999999  
10100          12.712871287128712  
10200          12.270588235294117  
10300          12.49864077669903   
10400          12.565384615384616  
10500          12.56               
10600          12.33056603773585   
10700          12.645981308411216  
10800          12.70888888888889   
10900          12.768440366972479  
11000          12.593454545454547  
11100          12.512432432432433  
11200          12.518571428571429  
11300          12.620176991150442  
11400          12.652631578947368  
11500          12.69495652173913   
11600          12.44896551724138   
11700          12.486153846153845  
11800          12.40677966101695   
11900          12.617142857142857  
12000          12.51               
12100          12.618842975206611  
12200          12.672786885245902  
12300          12.567804878048781  
12400          12.48967741935484   
12500          12.558720000000001  
12600          12.620952380952382  
12700          12.608503937007875  
12800          12.495              
12900          12.504186046511629  
13000          12.461538461538462  
13100          12.360916030534352  
13200          12.709090909090909  
13300          12.622556390977444  
13400          12.442388059701493  
13500          12.659555555555556  
13600          12.612352941176471  
13700          12.592116788321167  
13800          12.566956521739131  
13900          12.516258992805756  
14000          12.750857142857143  
14100          12.662127659574468  
14200          12.606760563380282  
14300          12.631048951048951  
14400          12.708333333333334  
14500          12.923586206896552  
14600          12.695342465753425  
14700          12.599183673469389  
14800          12.651891891891891  
14900          12.583087248322148  
15000          12.310500000000001  
15100          12.583311258278146  
15200          12.49421052631579   
15300          12.425098039215685  
15400          12.547012987012987  
15500          12.554322580645161  
15600          12.62923076923077   
15700          12.661910828025478  
15800          12.633417721518986  
15900          12.591698113207547  
16000          12.633000000000001  
16100          12.520248447204969  
16200          12.466666666666667  
16300          12.512392638036811  
16400          12.718536585365854  
16500          12.632727272727273  
16600          12.639036144578313  
16700          12.711377245508983  
16800          12.504285714285714  
16900          12.492781065088757  
17000          12.484235294117648  
17100          12.501052631578947  
17200          12.58046511627907   
17300          12.49664739884393   
17400          12.446896551724137  
17500          12.48               
17600          12.470454545454546  
17700          12.65491525423729   
17800          12.355955056179775  
17900          12.555083798882682  
18000          12.697333333333333  
18100          12.6046408839779    
18200          12.6210989010989    
18300          12.727868852459016  
18400          12.545217391304348  
18500          12.605837837837838  
18600          12.513548387096774  
18700          12.576256684491979  
18800          12.716170212765956  
18900          12.72               
19000          12.496421052631579  
19100          12.595602094240837  
19200          12.475              
19300          12.564559585492226  
19400          12.562886597938144  
19500          12.503384615384617  
19600          12.631836734693877  
19700          12.455634517766498  
19800          12.638787878787879  
19900          12.656080402010051  
20000          12.566399999999998  
20100          12.628059701492537  
20200          12.659405940594059  
20300          12.482364532019703  
20400          12.694117647058823  
20500          12.510439024390243  
20600          12.80504854368932   
20700          12.558840579710145  
20800          12.598846153846155  
20900          12.524784688995215  
21000          12.441142857142857  
21100          12.50047393364929   
21200          12.56490566037736   
21300          12.543098591549297  
21400          12.442990654205607  
21500          12.51013953488372   
21600          12.603333333333333  
21700          12.574009216589861  
21800          12.585688073394497  
21900          12.595068493150684  
22000          12.574909090909092  
22100          12.655927601809955  
22200          12.576216216216217  
22300          12.516591928251122  
22400          12.519642857142857  
22500          12.602666666666668  
22600          12.56495575221239   
22700          12.649162995594713  
22800          12.568421052631578  
22900          12.509344978165938  
23000          12.55095652173913   
23100          12.555844155844156  
23200          12.721034482758622  
23300          12.621115879828327  
23400          12.608205128205128  
23500          12.633191489361701  
23600          12.612203389830508  
23700          12.61873417721519   
23800          12.75126050420168   
23900          12.540251046025105  
24000          12.696              
24100          12.597510373443983  
24200          12.691239669421488  
24300          12.551111111111112  
24400          12.434754098360656  
24500          12.664163265306122  
24600          12.480975609756097  
24700          12.575222672064777  
24800          12.557419354838709  
24900          12.522409638554215  
25000          12.48864            
25100          12.61003984063745   
25200          12.553333333333333  
25300          12.531225296442686  
25400          12.564094488188976  
25500          12.534588235294118  
25600          12.6121875          
25700          12.541634241245136  
25800          12.631627906976744  
25900          12.536525096525097  
26000          12.648923076923076  
26100          12.531494252873562  
26200          12.534961832061068  
26300          12.594980988593155  
26400          12.616363636363637  
26500          12.691924528301886  
26600          12.640601503759399  
26700          12.61932584269663   
26800          12.685970149253732  
26900          12.635241635687732  
27000          12.519111111111112  
27100          12.583616236162362  
27200          12.562058823529412  
27300          12.676043956043957  
27400          12.454598540145986  
27500          12.680727272727273  
27600          12.57304347826087   
27700          12.564909747292418  
27800          12.60863309352518   
27900          12.563440860215053  
28000          12.533999999999999  
28100          12.646548042704627  
28200          12.572765957446808  
28300          12.540212014134276  
28400          12.69887323943662   
28500          12.544              
28600          12.594965034965035  
28700          12.493379790940766  
28800          12.568333333333333  
28900          12.680968858131488  
29000          12.601655172413793  
29100          12.541030927835052  
29200          12.598356164383562  
29300          12.661843003412969  
29400          12.53795918367347   
29500          12.578440677966102  
29600          12.635675675675675  
29700          12.769292929292929  
29800          12.569395973154363  
29900          12.482408026755854  
30000          12.525000000000001  
30100          12.600398671096347  
30200          12.567417218543046  
30300          12.54970297029703   
30400          12.431052631578947  
30500          12.481573770491803  
30600          12.548235294117646  
30700          12.695765472312704  
30800          12.640519480519481  
30900          12.623689320388351  
31000          12.53032258064516   
31100          12.608874598070738  
31200          12.521538461538462  
31300          12.65405750798722   
31400          12.630573248407643  
31500          12.754285714285714  
31600          12.559746835443038  
31700          12.601135646687696  
31800          12.551698113207546  
31900          12.521379310344827  
32000          12.516              
32100          12.56822429906542   
32200          12.574658385093167  
32300          12.535727554179566  
32400          12.46074074074074   
32500          12.54276923076923   
32600          12.66036809815951   
32700          12.539449541284403  
32800          12.630731707317073  
32900          12.657993920972643  
33000          12.423272727272726  
33100          12.533655589123867  
33200          12.640481927710844  
33300          12.561441441441442  
33400          12.661796407185628  
33500          12.583880597014927  
33600          12.423571428571428  
33700          12.504213649851632  
33800          12.5701775147929    
33900          12.527433628318585  
34000          12.550588235294118  
34100          12.601759530791789  
34200          12.647719298245613  
34300          12.540874635568514  
34400          12.585348837209303  
34500          12.703304347826087  
34600          12.638843930635838  
34700          12.581671469740634  
34800          12.635862068965515  
34900          12.546704871060172  
35000          12.47862857142857   
35100          12.549059829059829  
35200          12.567272727272728  
35300          12.343342776203965  
35400          12.713898305084747  
35500          12.491492957746479  
35600          12.604719101123594  
35700          12.540504201680672  
35800          12.56782122905028   
35900          12.580278551532034  
36000          12.566666666666666  
36100          12.581717451523547  
36200          12.62585635359116   
36300          12.462809917355372  
36400          12.602637362637363  
36500          12.485260273972603  
36600          12.44655737704918   
36700          12.56959128065395   
36800          12.607826086956523  
36900          12.578211382113821  
37000          12.680432432432431  
37100          12.551805929919137  
37200          12.557419354838709  
37300          12.581018766756033  
37400          12.608983957219252  
37500          12.54592            
37600          12.546382978723404  
37700          12.559575596816975  
37800          12.476825396825397  
37900          12.532559366754617  
38000          12.63978947368421   
38100          12.589606299212598  
38200          12.578638743455496  
38300          12.473107049608355  
38400          12.54625            
38500          12.577246753246753  
38600          12.500518134715024  
38700          12.540775193798451  
38800          12.656288659793814  
38900          12.50159383033419   
39000          12.508307692307692  
39100          12.585575447570331  
39200          12.603673469387754  
39300          12.589312977099237  
39400          12.533604060913706  
39500          12.582683544303798  
39600          12.573333333333334  
39700          12.628715365239294  
39800          12.446834170854272  
39900          12.586466165413533  
50000          12.6726             

Volume =  12.578382952779572

Fractional Error = 0.0076319681877811615
'''