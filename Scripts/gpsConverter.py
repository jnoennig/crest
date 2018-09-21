#encoding: utf-8

'''
Converts GPS degrees, minutes and seconds to decimal
coordinates
'''
import clipboard

print('Deliminate degrees, minutes, seconds and cardinal direction with comma.')
print('Example: 32,18,144,W')
lat_deg = input('Latitude in deg, min, sec, direction: ')
long_deg = input('Longitude in deg, min, sec, direction: ')

def convert_to_dec(degs, mins, secs, cd):
    '''
    '''
    expected_cds = ['n', 'e', 'w', 's']
    if cd.lower() not in expected_cds:
        print('The cardinal direction needs to be N, S, E, W')
    elif cd.lower() == 'w' or cd.lower() =='s':
        cd = -1
    else:
        cd = 1
    degs = int(degs)
    mins = int(mins)
    secs = int(secs)
    gps_dec = (degs + (mins/60) + (secs/3600)) * cd
    return gps_dec
    
def gps_split(gps_degs):
    '''
    '''
    (degs, mins, secs, cd) = gps_degs.split(',')
    gps_dict = {'degs': degs.strip(),
                'mins': mins.strip(),
                'secs': secs.strip(),
                'cd': cd.strip()}
    return gps_dict

def main():
    '''
    '''
    try:
        lat_split = gps_split(lat_deg)
        lat_dec = convert_to_dec(lat_split['degs'], lat_split['mins'], lat_split['secs'], lat_split['cd'])
        long_split = gps_split(long_deg)
        long_dec = convert_to_dec(long_split['degs'], long_split['mins'], long_split['secs'], long_split['cd'])
        print('Location (lat, long): {0}, {1}'.format(lat_dec, long_dec))
        loc_str = '{0}, {1}'.format(lat_dec, long_dec)
        clipboard.set(loc_str)
        print('Location copied to clipboard.')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
 