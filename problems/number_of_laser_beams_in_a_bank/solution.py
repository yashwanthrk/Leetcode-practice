class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        laser_beams = 0
        curr_floor = None

        for index in range(len(bank) - 1):
            
            if not curr_floor:
                curr_floor = bank[index]

            next_floor_devce = bank[index + 1].count("1")

            if next_floor_devce == 0:
                continue
            
            else:
                if curr_floor:
                    curr_floor_device = curr_floor.count("1")
                    laser_beams += (curr_floor_device * next_floor_devce)
                    curr_floor = None

            
        
        return laser_beams
                




        

        
        