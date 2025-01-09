
#define _USE_MATH_DEFINES

#include <cmath>

#include "generator.hpp"


std::uniform_real_distribution<> uniform(0., 1.);


class SamplerOne : public SamplerBase {
public:


    SamplerOne(int pid, double weight) 
        : SamplerBase(pid, weight) {
    }


    void sample() {

        static const double radius = 10.0;

        double cost = 1.0 - 2.0  * uniform(rand_state);
        double sint = std::sqrt((1.0 - cost) * (1.0 + cost));
        double phi  = 2.0 * M_PI * uniform(rand_state);
        double cosp = std::cos(phi);
        double sinp = std::sin(phi);

        x = sint * cosp * radius;
        y = sint * sinp * radius;
        z = cost * radius;

        // direction vector is negative
        u = -x;
        v = -y;
        w = -z;

        // translate to {-15, 0, 0}
        x -= 15.0;

        // direction vector normalization will be automatically applied.

        eke = 1.5;
        wee = 1.0;

    }


};


class SamplerTwo : public SamplerBase {
public:


    SamplerTwo(int pid, double weight)
        : SamplerBase(pid, weight) {
    }


    void sample() {

        static const double radius = 5.0;

        double cost = 1.0 - 2.0 * uniform(rand_state);
        double sint = std::sqrt((1.0 - cost) * (1.0 + cost));
        double phi  = 2.0 * M_PI * uniform(rand_state);
        double cosp = std::cos(phi);
        double sinp = std::sin(phi);

        x = sint * cosp * radius;
        y = sint * sinp * radius;
        z = cost * radius;

        // direction vector is negative
        u = -x;
        v = -y;
        w = -z;

        // translate to {15, 0, 0}
        x += 15.0;

        // direction vector normalization will be automatically applied.

        eke = 0.5;
        wee = 1.0;

    }


};


Generator::Generator() {

    SamplerOne* beam1 = new SamplerOne(0, 0.75);
    SamplerTwo* beam2 = new SamplerTwo(0, 0.25);

    this->registerBeam(beam1);
    this->registerBeam(beam2);

}
